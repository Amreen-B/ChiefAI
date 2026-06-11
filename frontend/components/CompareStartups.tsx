"use client";

import { useState } from "react";
import { compareReports } from "@/services/api";

type Props = {
  history?: any[];
};

export default function CompareStartups({
  history,
}: Props) {

  const reports = Array.isArray(history)
    ? history
    : [];

  const [report1, setReport1] =
    useState("");

  const [report2, setReport2] =
    useState("");

  const [comparison, setComparison] =
    useState<any>(null);

  async function handleCompare() {

    if (!report1 || !report2) {

      alert("Select two reports");
      return;

    }

    try {

      const result =
        await compareReports(
          Number(report1),
          Number(report2)
        );

      console.log(
        JSON.stringify(result, null, 2)
      );

      setComparison(result);

    } catch (err) {

      console.error(err);

      alert(
        "Comparison failed"
      );

    }

  }

  const reportA =
    comparison?.report1?.report_json || {};

  const reportB =
    comparison?.report2?.report_json || {};

  const scoreA =
    Number(
      reportA?.investor?.readiness_score || 0
    );

  const scoreB =
    Number(
      reportB?.investor?.readiness_score || 0
    );

  return (

    <div className="mt-10 bg-white rounded-2xl shadow-lg border border-gray-200 p-8">

      <h1 className="text-4xl font-bold text-gray-900 mb-8">
        Startup Comparison
      </h1>

      <div className="flex gap-5 items-center flex-wrap mb-8">

        <select
          value={report1}
          onChange={(e) =>
            setReport1(e.target.value)
          }
          className="
            border
            border-gray-300
            rounded-lg
            px-4
            py-3
            w-[280px]
            text-black
            bg-white
          "
        >
          <option value="">
            Select Report A
          </option>

          {reports.map((item) => (

            <option
              key={item.id}
              value={item.id}
            >
              Report #{item.id}
            </option>

          ))}
        </select>

        <select
          value={report2}
          onChange={(e) =>
            setReport2(e.target.value)
          }
          className="
            border
            border-gray-300
            rounded-lg
            px-4
            py-3
            w-[280px]
            text-black
            bg-white
          "
        >
          <option value="">
            Select Report B
          </option>

          {reports.map((item) => (

            <option
              key={item.id}
              value={item.id}
            >
              Report #{item.id}
            </option>

          ))}
        </select>

        <button
          onClick={handleCompare}
          className="
            bg-blue-600
            hover:bg-blue-700
            text-white
            px-8
            py-3
            rounded-lg
            font-semibold
          "
        >
          Compare
        </button>

      </div>

      {comparison && (

        <div className="mt-6 bg-white rounded-2xl border border-gray-200 shadow-lg p-8">

          <h2 className="text-3xl font-bold text-gray-900 mb-8">
            Startup Comparison Results
          </h2>

          <div className="overflow-x-auto">

            <table className="w-full">

              <thead>

                <tr className="bg-blue-600 text-white">

                  <th className="p-4 text-left">
                    Metric
                  </th>

                  <th className="p-4 text-center">
                    Report #{report1}
                  </th>

                  <th className="p-4 text-center">
                    Report #{report2}
                  </th>

                </tr>

              </thead>

              <tbody className="text-gray-900">

                <tr className="border-b">

                  <td className="p-4 font-semibold">
                    Market Size
                  </td>

                  <td className="p-4 text-center">
                    {reportA.market?.market_size || "-"}
                  </td>

                  <td className="p-4 text-center">
                    {reportB.market?.market_size || "-"}
                  </td>

                </tr>

                <tr className="border-b">

                  <td className="p-4 font-semibold">
                    Growth Rate
                  </td>

                  <td className="p-4 text-center">
                    {reportA.market?.growth_rate || "-"}
                  </td>

                  <td className="p-4 text-center">
                    {reportB.market?.growth_rate || "-"}
                  </td>

                </tr>

                <tr className="border-b">

                  <td className="p-4 font-semibold">
                    TAM
                  </td>

                  <td className="p-4 text-center">
                    {reportA.market?.tam || "-"}
                  </td>

                  <td className="p-4 text-center">
                    {reportB.market?.tam || "-"}
                  </td>

                </tr>

                <tr className="border-b">

                  <td className="p-4 font-semibold">
                    Investor Score
                  </td>

                  <td className="p-4 text-center text-blue-600 font-bold text-lg">
                    {reportA.investor?.readiness_score || "-"}
                  </td>

                  <td className="p-4 text-center text-green-600 font-bold text-lg">
                    {reportB.investor?.readiness_score || "-"}
                  </td>

                </tr>

                <tr className="border-b">

                  <td className="p-4 font-semibold">
                    Funding Stage
                  </td>

                  <td className="p-4 text-center">
                    {reportA.investor?.funding_stage || "-"}
                  </td>

                  <td className="p-4 text-center">
                    {reportB.investor?.funding_stage || "-"}
                  </td>

                </tr>

                <tr>

                  <td className="p-4 font-semibold">
                    Recommended Raise
                  </td>

                  <td className="p-4 text-center">
                    {reportA.investor?.recommended_raise || "-"}
                  </td>

                  <td className="p-4 text-center">
                    {reportB.investor?.recommended_raise || "-"}
                  </td>

                </tr>

              </tbody>

            </table>

          </div>

          <div className="mt-8 flex justify-center">

            <div
              className={`px-8 py-3 rounded-full text-white font-bold text-lg ${
                scoreA > scoreB
                  ? "bg-green-600"
                  : scoreB > scoreA
                  ? "bg-green-600"
                  : "bg-gray-500"
              }`}
            >
              {scoreA > scoreB
                ? `🏆 Report #${report1} Wins`
                : scoreB > scoreA
                ? `🏆 Report #${report2} Wins`
                : "🤝 Tie"}
            </div>

          </div>

        </div>

      )}

    </div>

  );

}