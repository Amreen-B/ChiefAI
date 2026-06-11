type Props = {
  report: any;
};

export default function InvestorReadiness({
  report,
}: Props) {

  const investor = report?.investor || {};

  return (

    <div className="space-y-6">

      <h1 className="text-3xl font-semibold text-black">
        Investor Readiness
      </h1>

      <div className="grid grid-cols-3 gap-4">

        <div className="bg-white p-5 rounded-xl shadow">
          <p className="text-black">
            Readiness Score
          </p>

          <h2 className="text-4xl font-bold text-green-600">
            {investor.readiness_score || 0}
          </h2>
        </div>

        <div className="bg-white p-5 rounded-xl shadow">
          <p className="text-black">
            Funding Stage
          </p>

          <h2 className="text-xl font-bold text-black">
            {investor.funding_stage || "N/A"}
          </h2>
        </div>

        <div className="bg-white p-5 rounded-xl shadow">
          <p className="text-black">
            Recommended Raise
          </p>

          <h2 className="text-xl font-bold text-black">
            {investor.recommended_raise || "N/A"}
          </h2>
        </div>

      </div>

      <div className="bg-white p-6 rounded-xl shadow">

        <h2 className="font-semibold text-lg mb-4 text-black">
          Strengths
        </h2>

        <ul className="list-disc ml-6 text-black">
          {(investor.strengths || []).map(
            (item: string, index: number) => (
              <li key={index}>{item}</li>
            )
          )}
        </ul>

      </div>

      <div className="bg-white p-6 rounded-xl shadow">

        <h2 className="font-semibold text-lg mb-4 text-black">
          Risks
        </h2>

        <ul className="list-disc ml-6 text-black">
          {(investor.risks || []).map(
            (item: string, index: number) => (
              <li key={index}>{item}</li>
            )
          )}
        </ul>

      </div>

    </div>

  );

}