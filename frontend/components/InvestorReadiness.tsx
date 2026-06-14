"use client";

// ── TypeScript Interfaces ──────────────────────────────────────────────────────

interface InvestorData {
  readiness_score?: string | number;
  funding_stage?: string;
  recommended_raise?: string;
  raise_amount?: string;
  strengths?: string[];
  weaknesses?: string[];
  risks?: string[];
  investment_risk?: string;
  recommendations?: string[];
}

interface AnalysisSummary {
  overall_score?: number;
  investment_outlook?: string;
  risk_level?: string;
  recommended_stage?: string;
}

interface Props {
  report: {
    investor?: InvestorData;
    analysis_summary?: AnalysisSummary;
    metadata?: {
      generated_at?: string;
    };
  } | null;
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function val(v: string | number | undefined, fallback = "N/A"): string {
  return v !== undefined && v !== null && String(v).trim() !== ""
    ? String(v)
    : fallback;
}

function arr(v: string[] | undefined): string[] {
  return Array.isArray(v) ? v : [];
}

function toNum(v: string | number | undefined): number {
  const n = parseFloat(String(v ?? ""));
  return isNaN(n) ? 0 : n;
}

function scoreColor(score: string | number | undefined): string {
  const n = toNum(score);
  if (n === 0) return "#605E5C";
  if (n >= 75) return "#107C10";
  if (n >= 50) return "#FF8C00";
  return "#D13438";
}

function riskColor(level: string | undefined): string {
  const l = (level ?? "").toLowerCase();
  if (l.includes("low"))    return "#107C10";
  if (l.includes("medium") || l.includes("moderate")) return "#FF8C00";
  if (l.includes("high"))   return "#D13438";
  return "#605E5C";
}

function riskBg(level: string | undefined): string {
  const l = (level ?? "").toLowerCase();
  if (l.includes("low"))    return "#DFF6DD";
  if (l.includes("medium") || l.includes("moderate")) return "#FFF4CE";
  if (l.includes("high"))   return "#FDE7E9";
  return "#F3F2F1";
}

function decisionFromScore(score: number): { label: string; icon: string; color: string; bg: string } {
  if (score >= 75) return { label: "Strong Invest",     icon: "✅", color: "#107C10", bg: "#DFF6DD" };
  if (score >= 50) return { label: "Consider Invest",   icon: "🟡", color: "#FF8C00", bg: "#FFF4CE" };
  return                  { label: "Needs Improvement", icon: "❌", color: "#D13438", bg: "#FDE7E9" };
}

// ── Reusable Components ───────────────────────────────────────────────────────

function SectionCard({
  icon,
  title,
  badge,
  children,
}: {
  icon: string;
  title: string;
  badge?: string;
  children: React.ReactNode;
}) {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200">
      <div className="flex items-center justify-between mb-5">
        <h2 className="text-xl font-bold text-[#323130] flex items-center gap-2">
          <span>{icon}</span>
          {title}
        </h2>
        {badge && (
          <span className="text-xs bg-[#E5F1FB] text-[#0078D4] px-3 py-1 rounded-full font-semibold">
            {badge}
          </span>
        )}
      </div>
      {children}
    </div>
  );
}

function KpiCard({
  icon,
  label,
  value,
  sub,
  accentColor,
  scoreValue,
  valueBg,
  valueColor,
}: {
  icon: string;
  label: string;
  value: string;
  sub?: string;
  accentColor: string;
  scoreValue?: number;
  valueBg?: string;
  valueColor?: string;
}) {
  return (
    <div
      className="bg-white rounded-xl shadow-sm border border-gray-200 p-5 hover:shadow-md hover:-translate-y-0.5 transition-all duration-200"
      style={{ borderTop: `4px solid ${accentColor}` }}
    >
      <div className="flex items-center gap-2 mb-2">
        <span className="text-xl">{icon}</span>
        <p className="text-xs uppercase tracking-wide text-[#605E5C] font-semibold">{label}</p>
      </div>
      <h2
        className="text-3xl font-bold leading-tight mt-1 px-2 py-0.5 rounded-lg inline-block"
        style={{
          color: valueColor ?? accentColor,
          backgroundColor: valueBg ?? "transparent",
        }}
      >
        {value}
      </h2>
      {sub && <p className="text-xs text-[#605E5C] mt-2">{sub}</p>}
      {scoreValue !== undefined && scoreValue > 0 && (
        <div className="mt-3">
          <div className="w-full bg-gray-100 rounded-full h-1.5">
            <div
              className="h-1.5 rounded-full transition-all duration-700"
              style={{
                width: `${Math.min(scoreValue, 100)}%`,
                backgroundColor: accentColor,
              }}
            />
          </div>
        </div>
      )}
    </div>
  );
}

function TagList({
  items,
  emptyText,
  icon = "›",
  iconClass = "text-[#0078D4]",
}: {
  items: string[];
  emptyText: string;
  icon?: string;
  iconClass?: string;
}) {
  if (items.length === 0)
    return <p className="text-sm text-[#605E5C]">{emptyText}</p>;
  return (
    <ul className="space-y-2">
      {items.map((item, i) => (
        <li key={i} className="flex items-start gap-2 text-sm text-[#323130] leading-6">
          <span className={`shrink-0 font-bold mt-0.5 ${iconClass}`}>{icon}</span>
          <span>{item}</span>
        </li>
      ))}
    </ul>
  );
}

function InfoRow({
  label,
  value,
  accentColor = "#0078D4",
}: {
  label: string;
  value: string;
  accentColor?: string;
}) {
  return (
    <div className="flex flex-col sm:flex-row sm:items-start gap-1 sm:gap-3 py-3 border-b border-gray-100 last:border-0">
      <span className="text-sm font-semibold sm:w-52 shrink-0" style={{ color: accentColor }}>
        {label}
      </span>
      <span className="text-[#323130] text-sm leading-6">{value}</span>
    </div>
  );
}

// ── Circular Score Ring ───────────────────────────────────────────────────────

function ScoreRing({
  score,
  max,
  label,
}: {
  score: string | number | undefined;
  max: number;
  label: string;
}) {
  const raw = toNum(score);
  const pct = max > 0 ? Math.min((raw / max) * 100, 100) : 0;
  const radius = 52;
  const circ = 2 * Math.PI * radius;
  const offset = circ - (pct / 100) * circ;
  const color = scoreColor(pct);

  return (
    <div className="flex flex-col items-center gap-2">
      <div className="relative w-32 h-32">
        <svg className="w-32 h-32 -rotate-90" viewBox="0 0 120 120">
          <circle cx="60" cy="60" r={radius} fill="none" stroke="#E5E5E5" strokeWidth="10" />
          <circle
            cx="60"
            cy="60"
            r={radius}
            fill="none"
            stroke={color}
            strokeWidth="10"
            strokeDasharray={circ}
            strokeDashoffset={offset}
            strokeLinecap="round"
          />
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className="text-3xl font-bold" style={{ color }}>
            {raw > 0 ? raw : "—"}
          </span>
          {raw > 0 && <span className="text-xs text-[#605E5C]">/{max}</span>}
        </div>
      </div>
      <p className="text-sm font-semibold text-[#323130] text-center">{label}</p>
    </div>
  );
}

// ── Main Component ────────────────────────────────────────────────────────────

export default function InvestorReadiness({ report }: Props) {

  if (!report) {
    return (
      <div className="flex flex-col items-center justify-center h-[60vh] gap-3">
        <span className="text-5xl">💰</span>
        <p className="text-[#605E5C] text-lg font-medium">No investor data available.</p>
        <p className="text-sm text-gray-400">Run an analysis to see investor readiness insights.</p>
      </div>
    );
  }

  const investor = report.investor ?? {};
  const summary  = report.analysis_summary ?? {};
  const metadata = report.metadata ?? {};

  const strengths      = arr(investor.strengths);
  const weaknesses     = arr(investor.weaknesses);
  const risks          = arr(investor.risks);
  const recommendations = arr(investor.recommendations);

  const raisedLabel = investor.recommended_raise ?? investor.raise_amount;

  // Risk level: prefer analysis_summary.risk_level, fall back to investor.investment_risk
  const riskLevel = summary.risk_level ?? investor.investment_risk;

  // Outlook: prefer analysis_summary.investment_outlook
  const outlook = summary.investment_outlook;

  const overallScore = toNum(summary.overall_score);
  const decision = decisionFromScore(overallScore);

  const generatedAt = metadata.generated_at
    ? new Date(metadata.generated_at).toLocaleString("en-US", { dateStyle: "medium", timeStyle: "short" })
    : null;

  return (
    <div className="space-y-8 text-gray-700">

      {/* ── Header ── */}
      <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-[#323130]">Investor Readiness</h1>
          <p className="text-sm text-[#605E5C] mt-1">
            AI-generated investor intelligence ·{" "}
            <span className="text-[#0078D4] font-medium">Investor Agent</span>
          </p>
          {generatedAt && (
            <p className="text-xs text-[#605E5C] mt-1">🕐 Generated: {generatedAt}</p>
          )}
        </div>
        <div className="flex flex-col gap-2 items-start sm:items-end">
          <span className="bg-[#E5F1FB] text-[#0078D4] px-4 py-2 rounded-full text-sm font-semibold whitespace-nowrap">
            ✦ Powered by Microsoft Azure AI Foundry
          </span>
          <span className="bg-[#DFF6DD] text-[#107C10] px-3 py-1 rounded-full text-xs font-semibold whitespace-nowrap">
            ✓ AI-Generated Analysis
          </span>
        </div>
      </div>

      {/* ── Score Rings + Decision Banner ── */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200">
        <div className="flex flex-col lg:flex-row items-center gap-8">

          {/* Score Rings */}
          <div className="flex flex-wrap justify-center gap-10">
            <ScoreRing score={investor.readiness_score} max={10}  label="Investment Readiness" />
            <ScoreRing score={summary.overall_score}     max={100} label="Overall Startup Score" />
          </div>

          {/* Decision Card */}
          <div className="flex-1 w-full space-y-4">

            {/* AI Investment Decision */}
            <div
              className="rounded-xl p-5 border-l-4 flex items-center gap-4"
              style={{ borderColor: decision.color, backgroundColor: decision.bg }}
            >
              <span className="text-4xl">{decision.icon}</span>
              <div>
                <p className="text-xs font-semibold text-[#605E5C] uppercase tracking-wide">
                  AI Investment Decision
                </p>
                <p className="text-2xl font-bold" style={{ color: decision.color }}>
                  {decision.label}
                </p>
              </div>
            </div>

            {/* Outlook + Risk side by side */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div className="bg-[#F3F2F1] rounded-xl p-4">
                <p className="text-xs font-semibold text-[#605E5C] uppercase tracking-wide mb-1">Investment Outlook</p>
                <p className="text-lg font-bold text-[#0078D4]">{val(outlook)}</p>
              </div>
              <div
                className="rounded-xl p-4"
                style={{ backgroundColor: riskBg(riskLevel) }}
              >
                <p className="text-xs font-semibold text-[#605E5C] uppercase tracking-wide mb-1">Risk Level</p>
                <p className="text-lg font-bold" style={{ color: riskColor(riskLevel) }}>
                  {val(riskLevel)}
                </p>
              </div>
            </div>

          </div>
        </div>
      </div>

      {/* ── KPI Cards ── */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <KpiCard
          icon="🎯"
          label="Overall Score"
          value={summary.overall_score !== undefined ? `${summary.overall_score}/100` : "N/A"}
          sub="Startup health"
          accentColor={scoreColor(summary.overall_score)}
          scoreValue={overallScore}
          valueColor={scoreColor(summary.overall_score)}
        />
        <KpiCard
          icon="💡"
          label="Readiness Score"
          value={investor.readiness_score !== undefined ? `${investor.readiness_score}/10` : "N/A"}
          sub="Investor Agent score"
          accentColor={scoreColor(toNum(investor.readiness_score) * 10)}
          scoreValue={toNum(investor.readiness_score) * 10}
          valueColor={scoreColor(toNum(investor.readiness_score) * 10)}
        />
        <KpiCard
          icon="🏦"
          label="Funding Stage"
          value={val(investor.funding_stage)}
          sub="Recommended"
          accentColor="#0078D4"
        />
        <KpiCard
          icon="💰"
          label="Raise Amount"
          value={val(raisedLabel)}
          sub="Target raise"
          accentColor="#107C10"
        />
      </div>

      {/* ── Funding Recommendation ── */}
      <SectionCard icon="🏦" title="Funding Recommendation">
        <div className="space-y-0">
          <InfoRow label="Funding Stage"     value={val(investor.funding_stage)} />
          <InfoRow label="Recommended Raise" value={val(raisedLabel)} accentColor="#107C10" />
          <InfoRow label="Investment Outlook" value={val(outlook)} accentColor="#8764B8" />
          <InfoRow label="Investment Risk"
            value={val(riskLevel)}
            accentColor={riskColor(riskLevel)}
          />
        </div>
      </SectionCard>

      {/* ── Investor Strengths & Weaknesses ── */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
        <SectionCard icon="💪" title="Strengths">
          <TagList items={strengths} emptyText="No strengths listed." icon="✅" iconClass="text-[#107C10]" />
        </SectionCard>
        <SectionCard icon="🛠️" title="Weaknesses">
          <TagList items={weaknesses} emptyText="No weaknesses listed." icon="⚠️" iconClass="text-[#FF8C00]" />
        </SectionCard>
      </div>

      {/* ── Investment Risks ── */}
      <SectionCard icon="⚠️" title="Investment Risks">
        <TagList items={risks} emptyText="No risks identified." icon="🔴" iconClass="text-[#D13438]" />
      </SectionCard>

      {/* ── AI Recommendations ── */}
      <SectionCard icon="🧠" title="AI Recommendations">
        {recommendations.length > 0 ? (
          <ol className="space-y-2">
            {recommendations.map((r, i) => (
              <li key={i} className="flex items-start gap-2 text-sm text-[#323130] leading-6 bg-[#F3F2F1] rounded-lg px-4 py-2">
                <span className="shrink-0 font-bold text-[#0078D4]">{i + 1}.</span>
                <span>{r}</span>
              </li>
            ))}
          </ol>
        ) : (
          <p className="text-sm text-[#605E5C]">No AI recommendations available.</p>
        )}
      </SectionCard>

      {/* ── Footer Branding ── */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-2 border-t border-gray-200">
        <p className="text-xs text-[#605E5C]">
          Powered by{" "}
          <span className="font-semibold text-[#0078D4]">Microsoft Azure AI Foundry</span>{" "}
          · Investor Agent
        </p>
        {generatedAt && (
          <p className="text-xs text-[#605E5C]">Report generated: {generatedAt}</p>
        )}
      </div>

    </div>
  );
}

