type Props = {
  report: any;
};

export default function BusinessStrategy({
  report,
}: Props) {

  const business = report?.business || {};

  return (

    <div className="space-y-6">

      <h1 className="text-3xl font-semibold text-black">
        Business Strategy
      </h1>

      <div className="bg-white p-6 rounded-xl shadow">

        <h2 className="font-semibold text-lg mb-2 text-black">
          Business Model
        </h2>

        <p className="text-black">
          {business.business_model}
        </p>

      </div>

      <div className="bg-white p-6 rounded-xl shadow">

        <h2 className="font-semibold text-lg mb-2 text-black">
          Target Customer
        </h2>

        <p className="text-black">
          {business.target_customer}
        </p>

      </div>

      <div className="bg-white p-6 rounded-xl shadow">

        <h2 className="font-semibold text-lg mb-2 text-black">
          Go To Market
        </h2>

        <p className="text-black">
          {business.go_to_market}
        </p>

      </div>

      <div className="bg-white p-6 rounded-xl shadow">

        <h2 className="font-semibold text-lg mb-2 text-black">
          Revenue Streams
        </h2>

        <ul className="list-disc ml-6 text-black">
          {(business.revenue_streams || []).map(
            (item: string, index: number) => (
              <li key={index}>{item}</li>
            )
          )}
        </ul>

      </div>

    </div>

  );

}