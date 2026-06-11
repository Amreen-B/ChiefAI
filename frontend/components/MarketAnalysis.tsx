type Props = {
  report: any;
};

export default function MarketAnalysis({
  report,
}: Props) {

  const market = report?.market || {};

  return (

    <div className="space-y-6">

      <h1 className="text-3xl font-semibold text-black">
        Market Analysis
      </h1>

      <div className="grid grid-cols-5 gap-4">

        <div className="bg-white p-5 rounded-xl shadow">
          <p className="text-black font-medium">
            Market Size
          </p>
          <h2 className="text-xl font-bold text-black">
            {market.market_size || "N/A"}
          </h2>
        </div>

        <div className="bg-white p-5 rounded-xl shadow">
          <p className="text-black font-medium">
            Growth Rate
          </p>
          <h2 className="text-xl font-bold text-black">
            {market.growth_rate || "N/A"}
          </h2>
        </div>

        <div className="bg-white p-5 rounded-xl shadow">
          <p className="text-black font-medium">
            TAM
          </p>
          <h2 className="text-xl font-bold text-black">
            {market.tam || "N/A"}
          </h2>
        </div>

        <div className="bg-white p-5 rounded-xl shadow">
          <p className="text-black font-medium">
            SAM
          </p>
          <h2 className="text-xl font-bold text-black">
            {market.sam || "N/A"}
          </h2>
        </div>

        <div className="bg-white p-5 rounded-xl shadow">
          <p className="text-black font-medium">
            SOM
          </p>
          <h2 className="text-xl font-bold text-black">
            {market.som || "N/A"}
          </h2>
        </div>

      </div>

      <div className="bg-white p-6 rounded-xl shadow">

        <h2 className="text-xl font-semibold mb-4 text-black">
          Competitors
        </h2>

        <ul className="list-disc ml-6 text-black">
          {(market.competitors || []).map(
            (item: string, index: number) => (
              <li key={index}>{item}</li>
            )
          )}
        </ul>

      </div>

      <div className="bg-white p-6 rounded-xl shadow-sm">
        <h2 className="text-xl font-semibold mb-4 text-black">
          Market Trends
        </h2>

        <ul className="list-disc ml-6 text-black">
          {(market.market_trends || []).map(
            (item: string, index: number) => (
              <li key={index}>{item}</li>
            )
          )}
        </ul>

      </div>

    </div>

  );

}