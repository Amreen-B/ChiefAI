"use client";

interface Competitor {
  name: string;
  strength: string;
}

interface MarketReport {
  metadata?: {
    generated_at?: string;
  };

  market?: {
    market_size?: string;
    growth_rate?: string;
    tam?: string;
    tam_explanation?: string;
    sam?: string;
    sam_explanation?: string;
    som?: string;
    som_explanation?: string;
    competitors?: Competitor[];
    market_trends?: string[];
    opportunities?: string[];
    risks?: string[];
  };
}

type Props = {
  report: MarketReport;
};

// ── Tooltip for TAM/SAM/SOM definitions ──────────────────────────────────────
function Tooltip({ text }: { text: string }) {
  return (
    <span className="group relative inline-flex">
      <span className="text-[#0078D4] text-xs font-bold border border-[#0078D4] rounded-full w-4 h-4 inline-flex items-center justify-center leading-none select-none">
        ?
      </span>
      <span className="absolute z-10 left-1/2 -translate-x-1/2 bottom-full mb-2 w-56 bg-[#323130] text-white text-xs rounded-lg px-3 py-2 opacity-0 group-hover:opacity-100 group-focus-within:opacity-100 transition-opacity pointer-events-none shadow-lg leading-5">
        {text}
      </span>
    </span>
  );
}

// ── Metric Card ───────────────────────────────────────────────────────────────
function MetricCard({
  label,
  value,
  sub,
  tooltip,
}: {
  label: string;
  value?: string;
  sub?: string;
  tooltip?: string;
}) {
  return (
    <div className="bg-white border border-gray-200 rounded-xl shadow-sm p-6 hover:shadow-md hover:-translate-y-1 transition-all duration-200 ease-in-out ease-in-out">

      <p className="text-xs uppercase tracking-wide text-[#605E5C] font-semibold flex items-center gap-1">
        {label}
        {tooltip && <Tooltip text={tooltip} />}
      </p>

      <h2 className="mt-3 text-4xl font-bold text-[#323130] leading-tight">
        {value ?? "Not Available"}
      </h2>

      {sub && (
        <p className="mt-2 text-sm text-[#605E5C] leading-6">
          {sub}
        </p>
      )}

    </div>
  );
}

// ── Section heading with optional icon ───────────────────────────────────────
function SectionHeading({ icon, title }: { icon: string; title: string }) {
  return (
    <h2 className="text-xl font-bold text-[#323130] mb-4 flex items-center gap-2">
      <span>{icon}</span>
      {title}
    </h2>
  );
}

// ── List item with icon ───────────────────────────────────────────────────────
function ListItem({ text, icon = "›" }: { text: string; icon?: string }) {
  return (
    <li className="flex items-start gap-2 text-gray-700 leading-7">
      <span className="mt-0.5 text-[#0078D4] font-bold shrink-0">{icon}</span>
      <span>{text}</span>
    </li>
  );
}

// ── Main Component ────────────────────────────────────────────────────────────
export default function MarketAnalysis({ report }: Props) {

  if (!report) {
    return (
      <div className="flex items-center justify-center h-[60vh]">
        <p className="text-[#605E5C]">Run an analysis first.</p>
      </div>
    );
  }

  const market = report.market || {};
  const metadata = report.metadata || {};

  const competitors = Array.isArray(market.competitors) ? market.competitors : [];
  const trends      = Array.isArray(market.market_trends) ? market.market_trends : [];
  const opportunities = Array.isArray(market.opportunities) ? market.opportunities : [];
  const risks       = Array.isArray(market.risks) ? market.risks : [];

  // Market Size split helper
  const marketSizeMain = market.market_size
    ? market.market_size.split("(")[0].trim()
    : "Not Available";

  const marketSizeSub = market.market_size?.includes("(")
    ? market.market_size
        .substring(
          market.market_size.indexOf("(") + 1,
          market.market_size.lastIndexOf(")")
        )
        .trim()
    : "Estimated Total Market";

  // Timestamp
  const generatedAt = metadata.generated_at
    ? new Date(metadata.generated_at).toLocaleString("en-US", {
        dateStyle: "medium",
        timeStyle: "short",
      })
    : null;

  return (
    <div className="space-y-8 text-gray-700 leading-8">

      {/* ── Header ── */}
      <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-3">

        <div>
          <h1 className="text-3xl font-bold text-[#323130]">
            Market Analysis
          </h1>
          <p className="text-sm text-[#605E5C] mt-1">
            AI-generated market intelligence powered by the{" "}
            <span className="font-medium text-[#0078D4]">Market Agent</span>{" "}
            · Microsoft Azure AI Foundry
          </p>
          {generatedAt && (
            <p className="text-xs text-[#605E5C] mt-1">
              Last updated: {generatedAt}
            </p>
          )}
        </div>

        <span className="self-start bg-[#E5F1FB] text-[#0078D4] px-4 py-2 rounded-full text-sm font-semibold whitespace-nowrap">
          Powered by Microsoft Azure AI Foundry
        </span>

      </div>

      {/* ── Metric Cards ── */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-5 gap-5">

        <MetricCard
          label="Market Size"
          value={marketSizeMain}
          sub={marketSizeSub}
        />

        <MetricCard
          label="Growth Rate"
          value={market.growth_rate || "Not Available"}
          sub="CAGR"
        />

        <MetricCard
          label="TAM"
          value={market.tam || "Not Available"}
          tooltip="Total Addressable Market — the total revenue opportunity if 100% market share were captured."
        />

        <MetricCard
          label="SAM"
          value={market.sam || "Not Available"}
          tooltip="Serviceable Available Market — the portion of TAM your product can realistically target."
        />

        <MetricCard
          label="SOM"
          value={market.som || "Not Available"}
          tooltip="Serviceable Obtainable Market — the realistic share you can capture in the near term."
        />

      </div>

      {/* ── Market Size Analysis ── */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200 ease-in-out">

        <SectionHeading icon="📊" title="Market Size Analysis" />

        <div className="space-y-5 text-gray-700 leading-8">

          {/* TAM */}
          <div>
            <p>
              <strong className="text-[#0078D4]">
                Total Addressable Market (TAM):
              </strong>{" "}
              {market.tam || "Not Available"}
            </p>
            <p className="text-[#605E5C] mt-1">
              {market.tam_explanation || "No explanation available."}
            </p>
          </div>

          {/* SAM */}
          <div>
            <p>
              <strong className="text-[#0078D4]">
                Serviceable Available Market (SAM):
              </strong>{" "}
              {market.sam || "Not Available"}
            </p>
            <p className="text-[#605E5C] mt-1">
              {market.sam_explanation || "No explanation available."}
            </p>
          </div>

          {/* SOM */}
          <div>
            <p>
              <strong className="text-[#0078D4]">
                Serviceable Obtainable Market (SOM):
              </strong>{" "}
              {market.som || "Not Available"}
            </p>
            <p className="text-[#605E5C] mt-1">
              {market.som_explanation || "No explanation available."}
            </p>
          </div>

        </div>

      </div>

      {/* ── Competitor Landscape ── */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200 ease-in-out">

        <div className="flex items-center justify-between mb-4">
          <SectionHeading icon="🏢" title="Competitor Landscape" />
          {competitors.length > 0 && (
            <span className="text-xs bg-[#E5F1FB] text-[#0078D4] px-3 py-1 rounded-full font-semibold">
              {competitors.length} identified
            </span>
          )}
        </div>

        <div className="space-y-4 text-gray-700 leading-8">

          {competitors.length > 0 ? (

            competitors.map((competitor: Competitor, index: number) => (

              <div
                key={index}
                className="bg-[#F3F2F1] border border-gray-200 rounded-xl p-5 hover:border-[#0078D4] hover:shadow-sm transition-all duration-200 ease-in-out"
              >

                <div className="flex items-center gap-2">
                  <span className="w-7 h-7 rounded-full bg-[#0078D4] text-white text-xs font-bold flex items-center justify-center shrink-0">
                    {index + 1}
                  </span>
                  <div className="text-lg font-semibold text-[#0078D4]">
                    {competitor.name || "Unnamed Competitor"}
                  </div>
                </div>

                <div className="text-[#605E5C] mt-2 leading-7 pl-9">
                  {competitor.strength || "No strength details available."}
                </div>

              </div>

            ))

          ) : (

            <p className="text-[#605E5C]">No competitors identified.</p>

          )}

        </div>

      </div>

      {/* ── Trends · Opportunities · Risks ── */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">

        {/* Market Trends */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200 ease-in-out">

          <SectionHeading icon="📈" title="Market Trends" />

          {trends.length > 0 ? (
            <ul className="space-y-3">
              {trends.map((item: string, index: number) => (
                <ListItem key={index} text={item} icon="→" />
              ))}
            </ul>
          ) : (
            <p className="text-[#605E5C] text-sm">No market trends identified.</p>
          )}

        </div>

        {/* Opportunities */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200 ease-in-out">

          <SectionHeading icon="🚀" title="Opportunities" />

          {opportunities.length > 0 ? (
            <ul className="space-y-3">
              {opportunities.map((item: string, index: number) => (
                <ListItem key={index} text={item} icon="✓" />
              ))}
            </ul>
          ) : (
            <p className="text-[#605E5C] text-sm">No opportunities identified.</p>
          )}

        </div>

        {/* Risks */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200 ease-in-out">

          <SectionHeading icon="⚠️" title="Risks" />

          {risks.length > 0 ? (
            <ul className="space-y-3">
              {risks.map((item: string, index: number) => (
                <ListItem key={index} text={item} icon="⚠" />
              ))}
            </ul>
          ) : (
            <p className="text-[#605E5C] text-sm">No risks identified.</p>
          )}

        </div>

      </div>

    </div>
  );
}


