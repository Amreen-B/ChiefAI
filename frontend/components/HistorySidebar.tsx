type Props = {
  history: any[];
  onSelect: (id: number) => void;
};

export default function HistorySidebar({
  history,
  onSelect,
}: Props) {

  return (

    <div className="bg-white border rounded-xl p-4">

      <h3 className="font-semibold mb-4 text-gray-700">
        Previous Analyses
      </h3>

      <div className="space-y-2">

        {history.map((item) => (

          <button
            key={item.id}
            onClick={() => onSelect(item.id)}
            className="
              w-full
              text-left
              p-3
              rounded-lg
              border
              hover:bg-gray-50
            "
          >
            Report #{item.id}
          </button>

        ))}

      </div>

    </div>

  );
}