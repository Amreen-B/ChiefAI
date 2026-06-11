type Props = {
  title: string;
  content: any;
};

export default function ReportCard({
  title,
  content,
}: Props) {
  return (
    <div className="border rounded-xl p-6 shadow">
      <h2 className="text-2xl font-bold mb-4">
        {title}
      </h2>

      <div className="whitespace-pre-wrap">
        <pre>
          {JSON.stringify(
            content,
            null,
            2
          )}
        </pre>
      </div>
    </div>
  );
}