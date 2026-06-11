"use client";

import Sidebar from "@/components/Sidebar";
import Topbar from "@/components/Topbar";
import TabPanel from "@/components/TabPanel";

import { useEffect, useState } from "react";

import {
  analyseStartup,
  uploadFile,
  getHistory,
  getReport,
} from "../services/api";

export default function Home() {

  const [file, setFile] =
    useState<File | null>(null);

  const [loading, setLoading] =
    useState(false);

  const [report, setReport] =
    useState<any>(null);

  const [history, setHistory] =
    useState<any[]>([]);

  const [selected, setSelected] =
    useState("Dashboard");

  useEffect(() => {

    getHistory()
      .then((data) => {

        console.log("HISTORY:");
        console.log(data);

        setHistory(data);

      })
      .catch(console.error);

  }, []);

  async function loadReport(
    id: number
  ) {

    try {

      const data =
        await getReport(id);

      console.log("LOADED REPORT:");
      console.log(data);

      setReport(data);

    } catch (err) {

      console.error(err);

    }

  }

  async function handleAnalyze() {

    if (!file) {
      alert("Select PDF first");
      return;
    }

    setLoading(true);

    try {

      console.log("START ANALYSIS");

      // Upload file

      const uploaded =
        await uploadFile(file);

      console.log("UPLOAD RESPONSE:");
      console.log(uploaded);

      if (!uploaded?.path) {

        console.error(
          "Upload API did not return a path"
        );

        alert(
          "Upload failed. No file path returned."
        );

        return;
      }

      console.log(
        "FILE PATH:",
        uploaded.path
      );

      // Run analysis

      const result =
        await analyseStartup(
          uploaded.path
        );

      console.log("ANALYSIS RESULT:");
      console.log(result);

      setReport(result);

      // Refresh history

      const updatedHistory =
        await getHistory();

      setHistory(updatedHistory);

    } catch (err) {

      console.error(
        "ANALYSIS ERROR:",
        err
      );

      alert(
        "Analysis failed. Check backend terminal."
      );

    } finally {

      setLoading(false);

    }

  }

  console.log("CURRENT REPORT", report); 
  return (

    <main className="h-screen bg-[#f5f6f8]">

      <Topbar />

      <div className="flex h-[calc(100vh-72px)] overflow-hidden">


        <Sidebar
          selected={selected}
          setSelected={setSelected}
          history={history}
          onSelectHistory={loadReport}
          currentReport={report}
        />

        <div className="flex-1 overflow-y-auto bg-[#f5f6f8] p-6">

          <div className="flex gap-4 mb-8 items-center">

            <input
              type="file"
              accept=".pdf"
              onChange={(e) => {

                if (
                  e.target.files &&
                  e.target.files[0]
                ) {

                  setFile(
                    e.target.files[0]
                  );

                }

              }}
              className="
                bg-white
                border
                rounded-lg
                p-2
              "
            />

            <button
              onClick={handleAnalyze}
              className="
                bg-blue-600
                hover:bg-blue-700
                text-white
                px-6
                py-2
                rounded-lg
              "
            >
              {
                loading
                  ? "Analyzing..."
                  : "Analyze Startup"
              }
            </button>

          </div>

          <TabPanel
            selected={selected}
            report={report}
            history={history}
          />

        </div>

      </div>

    </main>

  );

}