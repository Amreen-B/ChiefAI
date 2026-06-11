type Props = {
  report: any;
};

export default function Dashboard({
  report,
}: Props) {

  return (

    <div className="space-y-6">
      <div className="space-y-6">

      {/* AI Insight */}

      <div
        className="
          bg-[#eef5fd]
          border-l-4
          border-[#0f6cbd]
          p-5
          rounded-md
        "
      >

        <h3 className="font-semibold text-[#0f6cbd] text-lg">
          AI Insight
        </h3>

        <p className="text-[#323130] mt-1">
          Startup analysis completed successfully.
        </p>

      </div>

      {/* KPI Cards */}

      <div className="grid grid-cols-4 gap-5">

        <div className="bg-white rounded-xl shadow-sm p-6 border-t-4 border-blue-500">

          <p className="text-gray-500 text-sm">
            Market Size
          </p>

          <h2 className="text-3xl font-semibold text-black mt-2">
            {String(report?.market?.market_size || "-").slice(0, 25)}
          </h2>

        </div>

        <div className="bg-white rounded-xl shadow-sm p-6 border-t-4 border-green-500">

          <p className="text-gray-500 text-sm">
            Growth Rate
          </p>

          <h2 className="text-3xl font-semibold text-black mt-2">
            {String(report?.market?.growth_rate || "-").slice(0, 25)}
          </h2>

        </div>

        <div className="bg-white rounded-xl shadow-sm p-6 border-t-4 border-purple-500">

          <p className="text-gray-500 text-sm">
            Investor Score
          </p>

          <h2 className="text-3xl font-semibold text-black mt-2">
            {String(report?.investor?.readiness_score || "-").slice(0, 25)}
          </h2>

        </div>

        <div className="bg-white rounded-xl shadow-sm p-6 border-t-4 border-orange-500">

          <p className="text-gray-500 text-sm">
            Competitors
          </p>

          <h2 className="text-3xl font-semibold text-black mt-2">
            {String(report?.market?.competitors?.length || "-").slice(0, 25)}
          </h2>

        </div>

      </div>

      {/* Executive Overview */}

      <div className="bg-white rounded-xl shadow-sm p-8">

        <h2 className="text-3xl font-semibold text-black mb-6">
          Executive Overview
        </h2>

        <div className="space-y-4 text-[17px] text-[#323130]">

          <p>
            <strong>Market Size:</strong>{" "}
            {String(report?.market?.market_size || "-").slice(0, 25)}
          </p>

          <p>
            <strong>Growth Rate:</strong>{" "}
            {String(report?.market?.growth_rate || "-").slice(0, 25)}
          </p>

          <p>
            <strong>Investor Score:</strong>{" "}
            {String(report?.investor?.readiness_score || "-").slice(0, 25)}
          </p>

          <p>
            <strong>Competitors:</strong>{" "}
            {String(report?.market?.competitors?.join(", ") || "-").slice(0, 25)}
          </p>

        </div>

      </div>
      </div>

    </div>

  );

}