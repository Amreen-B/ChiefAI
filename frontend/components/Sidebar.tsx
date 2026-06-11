import {
  MdDashboard,
  MdAnalytics,
  MdBusiness,
  MdPeople,
  MdCompareArrows,
  MdDescription,
  MdFileDownload,
} from "react-icons/md";

import { useState } from "react";
import { exportReport as exportPdfReport } from "@/services/api";

type Props = {
  selected: string;
  setSelected: (value: string) => void;
  history: any[];
  onSelectHistory: (id: number) => void;
  currentReport?: any;
};

const menuItems = [
  {
    label: "Dashboard",
    icon: <MdDashboard size={20} />,
  },
  {
    label: "Market Analysis",
    icon: <MdAnalytics size={20} />,
  },
  {
    label: "Business Strategy",
    icon: <MdBusiness size={20} />,
  },
  {
    label: "Investor Readiness",
    icon: <MdPeople size={20} />,
  },
  {
    label: "Compare Startups",
    icon: <MdCompareArrows size={20} />,
  },
];

export default function Sidebar({
  selected,
  setSelected,
  history,
  onSelectHistory,
  currentReport,
}: Props) {
  const [activeReportId, setActiveReportId] =
    useState<number | null>(null);


  return (
    <aside
      className="
        w-[290px]
        bg-[#f7f7f7]
        border-r
        border-[#e1dfdd]
        flex
        flex-col
        h-full
        overflow-y-auto
      "
    >
      {/* WORKSPACE */}

      <div className="px-6 pt-6">
        <p
          className="
            text-[13px]
            font-bold
            text-[#8a8886]
            uppercase
            tracking-wide
            mb-3
          "
        >
          Workspace
        </p>

        <div className="space-y-2">
          {menuItems.map((item) => (
            <button
              key={item.label}
              onClick={() =>
                setSelected(item.label)
              }
              className={`
                w-full
                flex
                items-center
                gap-4
                px-6
                py-3
                rounded-lg
                text-left
                transition
                ${
                  selected === item.label
                    ? "bg-[#e8f1fb] text-[#0f6cbd] border-l-4 border-[#0f6cbd]"
                    : "text-[#323130] hover:bg-[#f0f0f0]"
                }
              `}
            >
              {item.icon}

              <span className="text-[16px]">
                {item.label}
              </span>
            </button>
          ))}
        </div>
      </div>

      {/* REPORTS */}

      <div className="px-6 mt-8">
        <p className="text-[13px] 
        font-bold 
        text-[#8a8886] 
        uppercase
        mb-3">
          Reports
        </p>

        <div className="space-y-3">
          <button
            onClick={() => {
              
            const reportId =
              currentReport?.id ||
              history?.[0]?.id;

            if (!reportId) {

              alert("No report available");
              return;

            }

            exportPdfReport(reportId);

          }}
            className="
              w-full
              flex
              items-center
              gap-3
              px-5
              py-3
              bg-white
              rounded-lg
              border
              border-gray-300
              hover:bg-blue-50
              text-sm
              font-medium
              text-gray-700
              shadow-sm
              transition
            "
          >
            <MdFileDownload size={18} />
            Export Data
          </button>
        </div>
      </div>

      {/* HISTORY */}

      <div className="px-6 mt-8 pb-8">
        <p className="text-[13px] font-bold text-[#8a8886] uppercase mb-3">
          Previous Analyses
        </p>

        <div className="space-y-2">

          {history &&
          history.length > 0 ? (

            history
              .slice(0, 3)
              .map((item) => (

                <button
                  key={item.id}
                  onClick={() => {

                    setActiveReportId(
                      item.id
                    );

                    onSelectHistory(
                      item.id
                    );

                  }}
                  className={`
                    w-full
                    flex
                    items-center
                    gap-3
                    px-5
                    py-3
                    rounded-lg
                    border
                    text-sm
                    font-medium
                    shadow-sm
                    transition

                    ${
                      activeReportId ===
                      item.id
                        ? "bg-blue-100 border-blue-400 text-blue-700"
                        : "bg-white border-gray-300 text-gray-700 hover:bg-blue-50"
                    }
                  `}
                >
                  <MdDescription
                    size={18}
                  />

                  {item.startup_name
                    ? item.startup_name
                    : `Report #${item.id}`}
                </button>

              ))

          ) : (

            <div className="text-sm text-gray-500">
              No reports yet
            </div>

          )}

        </div>

        {history?.length > 3 && (
          <div className="mt-3 text-xs text-gray-500">
            Showing latest 3 analyses
          </div>
        )}
      </div>
    </aside>
  );
}