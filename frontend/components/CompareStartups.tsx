// "use client";

// import { useState } from "react";
// import { compareReports } from "@/services/api";

// // ── TypeScript Interfaces ──────────────────────────────────────────────────────

// interface HistoryItem {
//   id: number;
//   created_at?: string;
//   startup_name?: string;
//   report_json?: ReportJson;
// }

// interface ReportJson {
//   market?: {
//     market_size?: string;
//     growth_rate?: string;
//     tam?: string;
//     sam?: string;
//     som?: string;
//     opportunities?: string[];
//   };
//   business?: {
//     business_model?: string;
//     target_customer?: string;
//     revenue_streams?: string[];
//     pricing_strategy?: string;
//     go_to_market?: string;
//     strengths?: string[];
//     weaknesses?: string[];
//     opportunities?: string[];
//     threats?: string[];
//   };
//   investor?: {
//     readiness_score?: string | number;
//     overall_score?: string | number;
//     ai_confidence?: string | number;
//     investment_outlook?: string;
//     risk_level?: string;
//     funding_stage?: string;
//     recommended_raise?: string;
//     raise_amount?: string;
//     risks?: string[];
//     market_risks?: string[];
//     technology_risks?: string[];
//     operational_risks?: string[];
//   };
//   overview?: {
//     overall_score?: string | number;
//     ai_confidence?: string | number;
//     executive_summary?: string;
//   };
// }

// interface ComparisonResult {
//   report1?: {
//     id?: number;
//     report_json?: ReportJson;
//     startup_name?: string;
//     created_at?: string;
//   };
//   report2?: {
//     id?: number;
//     report_json?: ReportJson;
//     startup_name?: string;
//     created_at?: string;
//   };
//   ai_verdict?: {
//     winner?: string;
//     reason?: string;
//     startup_a_strengths?: string[];
//     startup_b_strengths?: string[];
//     recommendation?: string;
//     investment_preference?: string;
//   };
// }

// interface Props {
//   history?: HistoryItem[];
// }

// // ── Helpers ───────────────────────────────────────────────────────────────────

// function val(v: string | number | undefined, fallback = "N/A"): string {
//   return v !== undefined && v !== null && String(v).trim() !== ""
//     ? String(v)
//     : fallback;
// }

// function toNum(v: string | number | undefined): number {
//   const n = parseFloat(String(v ?? ""));
//   return isNaN(n) ? 0 : n;
// }

// function arr(v: string[] | undefined): string[] {
//   return Array.isArray(v) ? v : [];
// }

// function fmtDate(d: string | undefined): string {
//   if (!d) return "";
//   try {
//     return new Date(d).toLocaleDateString("en-US", { dateStyle: "medium" });
//   } catch {
//     return d;
//   }
// }

// // Score-based comparison — returns which side "wins" for a numeric metric
// function numWinner(a: string | number | undefined, b: string | number | undefined): "A" | "B" | "tie" {
//   const na = toNum(a), nb = toNum(b);
//   if (na === 0 && nb === 0) return "tie";
//   if (na > nb) return "A";
//   if (nb > na) return "B";
//   return "tie";
// }

// // Generic text winner — just checks if values are present / identical
// function textWinner(a: string | undefined, b: string | undefined): "tie" {
//   return "tie";
// }

// function scoreColor(v: string | number | undefined, fallback = "#605E5C"): string {
//   const n = toNum(v);
//   if (n === 0) return fallback;
//   if (n >= 75) return "#107C10";
//   if (n >= 50) return "#FF8C00";
//   return "#D13438";
// }

// function scoreBg(v: string | number | undefined): string {
//   const n = toNum(v);
//   if (n === 0) return "#F3F2F1";
//   if (n >= 75) return "#DFF6DD";
//   if (n >= 50) return "#FFF4CE";
//   return "#FDE7E9";
// }

// function riskColor(level: string | undefined): string {
//   const l = (level ?? "").toLowerCase();
//   if (l.includes("low"))    return "#107C10";
//   if (l.includes("medium")) return "#FF8C00";
//   if (l.includes("high"))   return "#D13438";
//   return "#605E5C";
// }

// // ── Reusable Components ───────────────────────────────────────────────────────

// function SectionCard({
//   icon,
//   title,
//   children,
// }: {
//   icon: string;
//   title: string;
//   children: React.ReactNode;
// }) {
//   return (
//     <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-all duration-200">
//       <div className="bg-[#F3F2F1] border-b border-gray-200 px-6 py-4 flex items-center gap-2">
//         <span className="text-lg">{icon}</span>
//         <h3 className="text-base font-bold text-[#323130]">{title}</h3>
//       </div>
//       <div className="p-0">{children}</div>
//     </div>
//   );
// }

// // Side A = blue, Side B = green — winner gets bold highlight
// function CompareRow({
//   label,
//   valueA,
//   valueB,
//   winner,
//   isScore = false,
//   scoreA,
//   scoreB,
// }: {
//   label: string;
//   valueA: string;
//   valueB: string;
//   winner: "A" | "B" | "tie";
//   isScore?: boolean;
//   scoreA?: number;
//   scoreB?: number;
// }) {
//   const cellBase = "p-4 text-center text-sm align-top";
//   const winStyle = "font-bold text-[#107C10]";
//   const loseStyle = "text-[#605E5C]";
//   const tieStyle = "text-[#323130]";

//   return (
//     <tr className="border-b border-gray-100 hover:bg-[#F9F9F9] transition-colors">
//       <td className="p-4 text-sm font-semibold text-[#323130] align-top w-1/4">
//         {label}
//       </td>
//       <td className={`${cellBase} ${winner === "A" ? winStyle : winner === "B" ? loseStyle : tieStyle}`}>
//         <div className="flex flex-col items-center gap-1">
//           {winner === "A" && (
//             <span className="text-xs bg-[#DFF6DD] text-[#107C10] px-2 py-0.5 rounded-full font-semibold mb-1">
//               ▲ Stronger
//             </span>
//           )}
//           {winner === "B" && (
//             <span className="text-xs bg-[#FDE7E9] text-[#D13438] px-2 py-0.5 rounded-full font-semibold mb-1">
//               ▼ Weaker
//             </span>
//           )}
//           <span>{valueA}</span>
//           {isScore && scoreA !== undefined && scoreA > 0 && (
//             <div className="w-20 bg-gray-100 rounded-full h-1.5 mt-1">
//               <div
//                 className="h-1.5 rounded-full"
//                 style={{ width: `${Math.min(scoreA, 100)}%`, backgroundColor: scoreColor(scoreA) }}
//               />
//             </div>
//           )}
//         </div>
//       </td>
//       <td className={`${cellBase} ${winner === "B" ? winStyle : winner === "A" ? loseStyle : tieStyle}`}>
//         <div className="flex flex-col items-center gap-1">
//           {winner === "B" && (
//             <span className="text-xs bg-[#DFF6DD] text-[#107C10] px-2 py-0.5 rounded-full font-semibold mb-1">
//               ▲ Stronger
//             </span>
//           )}
//           {winner === "A" && (
//             <span className="text-xs bg-[#FDE7E9] text-[#D13438] px-2 py-0.5 rounded-full font-semibold mb-1">
//               ▼ Weaker
//             </span>
//           )}
//           <span>{valueB}</span>
//           {isScore && scoreB !== undefined && scoreB > 0 && (
//             <div className="w-20 bg-gray-100 rounded-full h-1.5 mt-1">
//               <div
//                 className="h-1.5 rounded-full"
//                 style={{ width: `${Math.min(scoreB, 100)}%`, backgroundColor: scoreColor(scoreB) }}
//               />
//             </div>
//           )}
//         </div>
//       </td>
//     </tr>
//   );
// }

// function ListCompareRow({
//   label,
//   itemsA,
//   itemsB,
// }: {
//   label: string;
//   itemsA: string[];
//   itemsB: string[];
// }) {
//   return (
//     <tr className="border-b border-gray-100 hover:bg-[#F9F9F9] transition-colors">
//       <td className="p-4 text-sm font-semibold text-[#323130] align-top w-1/4">{label}</td>
//       <td className="p-4 align-top">
//         {itemsA.length > 0 ? (
//           <ul className="space-y-1">
//             {itemsA.slice(0, 3).map((item, i) => (
//               <li key={i} className="flex items-start gap-1.5 text-xs text-[#323130]">
//                 <span className="text-[#0078D4] shrink-0 mt-0.5">›</span>
//                 {item}
//               </li>
//             ))}
//             {itemsA.length > 3 && (
//               <li className="text-xs text-[#605E5C]">+{itemsA.length - 3} more</li>
//             )}
//           </ul>
//         ) : (
//           <span className="text-xs text-[#605E5C]">N/A</span>
//         )}
//       </td>
//       <td className="p-4 align-top">
//         {itemsB.length > 0 ? (
//           <ul className="space-y-1">
//             {itemsB.slice(0, 3).map((item, i) => (
//               <li key={i} className="flex items-start gap-1.5 text-xs text-[#323130]">
//                 <span className="text-[#107C10] shrink-0 mt-0.5">›</span>
//                 {item}
//               </li>
//             ))}
//             {itemsB.length > 3 && (
//               <li className="text-xs text-[#605E5C]">+{itemsB.length - 3} more</li>
//             )}
//           </ul>
//         ) : (
//           <span className="text-xs text-[#605E5C]">N/A</span>
//         )}
//       </td>
//     </tr>
//   );
// }

// function TableHeader({
//   nameA,
//   idA,
//   nameB,
//   idB,
// }: {
//   nameA: string;
//   idA: string;
//   nameB: string;
//   idB: string;
// }) {
//   return (
//     <thead>
//       <tr>
//         <th className="p-4 text-left text-sm font-semibold text-[#605E5C] bg-[#F3F2F1] w-1/4">
//           Metric
//         </th>
//         <th className="p-4 text-center bg-[#E5F1FB] border-b-4 border-[#0078D4]">
//           <div className="flex flex-col items-center gap-1">
//             <span className="text-lg">🅰️</span>
//             <span className="text-sm font-bold text-[#0078D4]">{nameA}</span>
//             <span className="text-xs text-[#605E5C]">Report #{idA}</span>
//           </div>
//         </th>
//         <th className="p-4 text-center bg-[#DFF6DD] border-b-4 border-[#107C10]">
//           <div className="flex flex-col items-center gap-1">
//             <span className="text-lg">🅱️</span>
//             <span className="text-sm font-bold text-[#107C10]">{nameB}</span>
//             <span className="text-xs text-[#605E5C]">Report #{idB}</span>
//           </div>
//         </th>
//       </tr>
//     </thead>
//   );
// }

// // ── Main Component ────────────────────────────────────────────────────────────

// export default function CompareStartups({ history }: Props) {

//   const reports = Array.isArray(history) ? history : [];

//   const [report1, setReport1] = useState("");
//   const [report2, setReport2] = useState("");
//   const [comparison, setComparison] = useState<ComparisonResult | null>(null);
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState<string | null>(null);

//   async function handleCompare() {
//     if (!report1 || !report2) {
//       setError("Please select two different reports to compare.");
//       return;
//     }
//     if (report1 === report2) {
//       setError("Please select two different reports.");
//       return;
//     }
//     setError(null);
//     setLoading(true);
//     try {
//       const result = await compareReports(Number(report1), Number(report2));
//       setComparison(result);
//     } catch (err) {
//       console.error(err);
//       setError("Comparison failed. Please try again.");
//     } finally {
//       setLoading(false);
//     }
//   }

//   const reportA: ReportJson = comparison?.report1?.report_json ?? {};
//   const reportB: ReportJson = comparison?.report2?.report_json ?? {};
//   const nameA = comparison?.report1?.startup_name ?? `Report #${report1}`;
//   const nameB = comparison?.report2?.startup_name ?? `Report #${report2}`;
//   const dateA = fmtDate(comparison?.report1?.created_at);
//   const dateB = fmtDate(comparison?.report2?.created_at);

//   // Scores for winner logic
//   const overallA  = toNum(reportA.overview?.overall_score  ?? reportA.investor?.overall_score);
//   const overallB  = toNum(reportB.overview?.overall_score  ?? reportB.investor?.overall_score);
//   const readyA    = toNum(reportA.investor?.readiness_score);
//   const readyB    = toNum(reportB.investor?.readiness_score);
//   const confA     = toNum(reportA.overview?.ai_confidence  ?? reportA.investor?.ai_confidence);
//   const confB     = toNum(reportB.overview?.ai_confidence  ?? reportB.investor?.ai_confidence);

//   // Determine overall winner (sum of weighted scores)
//   const totalA = overallA * 0.4 + readyA * 0.4 + confA * 0.2;
//   const totalB = overallB * 0.4 + readyB * 0.4 + confB * 0.2;
//   const overallWinner =
//     totalA > totalB ? "A" : totalB > totalA ? "B" : "tie";

//   const verdict = comparison?.ai_verdict;

//   // ── No reports guard ──
//   if (reports.length === 0) {
//     return (
//       <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-12 text-center space-y-3">
//         <span className="text-5xl">📊</span>
//         <p className="text-lg font-semibold text-[#323130]">No reports available</p>
//         <p className="text-sm text-[#605E5C]">
//           Run at least two startup analyses to unlock the comparison feature.
//         </p>
//       </div>
//     );
//   }

//   if (reports.length === 1) {
//     return (
//       <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-12 text-center space-y-3">
//         <span className="text-5xl">📊</span>
//         <p className="text-lg font-semibold text-[#323130]">Only one report available</p>
//         <p className="text-sm text-[#605E5C]">
//           Analyze a second startup to compare side by side.
//         </p>
//       </div>
//     );
//   }

//   return (
//     <div className="space-y-8">

//       {/* ── Header ── */}
//       <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
//         <div>
//           <h1 className="text-3xl font-bold text-[#323130]">Startup Comparison</h1>
//           <p className="text-sm text-[#605E5C] mt-1">
//             AI-powered side-by-side analysis ·{" "}
//             <span className="text-[#0078D4] font-medium">Comparison Agent</span>
//           </p>
//         </div>
//         <div className="flex flex-col gap-2 items-start sm:items-end">
//           <span className="bg-[#E5F1FB] text-[#0078D4] px-4 py-2 rounded-full text-sm font-semibold whitespace-nowrap">
//             ✦ Microsoft Azure AI Foundry
//           </span>
//           <span className="bg-[#DFF6DD] text-[#107C10] px-3 py-1 rounded-full text-xs font-semibold whitespace-nowrap">
//             ✓ AI-Generated Comparison
//           </span>
//         </div>
//       </div>

//       {/* ── Selection Panel ── */}
//       <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
//         <h2 className="text-base font-bold text-[#323130] mb-4 flex items-center gap-2">
//           <span>🔍</span> Select Startups to Compare
//         </h2>

//         <div className="flex flex-col sm:flex-row gap-4 items-start sm:items-end flex-wrap">

//           {/* Dropdown A */}
//           <div className="flex flex-col gap-1">
//             <label className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide">
//               Startup A
//             </label>
//             <select
//               value={report1}
//               onChange={(e) => { setReport1(e.target.value); setError(null); }}
//               className="border border-gray-300 rounded-lg px-4 py-3 w-72 text-[#323130] bg-white focus:outline-none focus:border-[#0078D4] focus:ring-1 focus:ring-[#0078D4] transition"
//             >
//               <option value="">Select Report A</option>
//               {reports.map((item) => (
//                 <option
//                   key={item.id}
//                   value={item.id}
//                   disabled={String(item.id) === report2}
//                 >
//                   {item.startup_name ? `${item.startup_name} (#${item.id})` : `Report #${item.id}`}
//                   {item.created_at ? ` · ${fmtDate(item.created_at)}` : ""}
//                 </option>
//               ))}
//             </select>
//           </div>

//           <div className="text-2xl text-[#605E5C] font-bold sm:mb-3">vs</div>

//           {/* Dropdown B */}
//           <div className="flex flex-col gap-1">
//             <label className="text-xs font-semibold text-[#107C10] uppercase tracking-wide">
//               Startup B
//             </label>
//             <select
//               value={report2}
//               onChange={(e) => { setReport2(e.target.value); setError(null); }}
//               className="border border-gray-300 rounded-lg px-4 py-3 w-72 text-[#323130] bg-white focus:outline-none focus:border-[#107C10] focus:ring-1 focus:ring-[#107C10] transition"
//             >
//               <option value="">Select Report B</option>
//               {reports.map((item) => (
//                 <option
//                   key={item.id}
//                   value={item.id}
//                   disabled={String(item.id) === report1}
//                 >
//                   {item.startup_name ? `${item.startup_name} (#${item.id})` : `Report #${item.id}`}
//                   {item.created_at ? ` · ${fmtDate(item.created_at)}` : ""}
//                 </option>
//               ))}
//             </select>
//           </div>

//           <button
//             onClick={handleCompare}
//             disabled={loading || !report1 || !report2 || report1 === report2}
//             className="bg-[#0078D4] hover:bg-[#006CBD] disabled:opacity-50 disabled:cursor-not-allowed text-white px-8 py-3 rounded-lg font-semibold transition-all duration-200 sm:mb-0 flex items-center gap-2"
//           >
//             {loading ? (
//               <>
//                 <span className="animate-spin">⟳</span> Comparing…
//               </>
//             ) : (
//               <>⚡ Compare</>
//             )}
//           </button>
//         </div>

//         {error && (
//           <div className="mt-4 bg-[#FDE7E9] border border-[#D13438] text-[#D13438] rounded-lg px-4 py-3 text-sm font-medium">
//             ⚠️ {error}
//           </div>
//         )}
//       </div>

//       {/* ── Results ── */}
//       {comparison && (
//         <div className="space-y-6">

//           {/* ── Winner Banner ── */}
//           <div
//             className="rounded-xl p-6 border-l-4 flex flex-col sm:flex-row items-start sm:items-center gap-5"
//             style={{
//               borderColor: overallWinner === "tie" ? "#605E5C" : "#107C10",
//               backgroundColor: overallWinner === "tie" ? "#F3F2F1" : "#DFF6DD",
//             }}
//           >
//             <span className="text-5xl shrink-0">
//               {overallWinner === "tie" ? "🤝" : "🏆"}
//             </span>
//             <div className="flex-1">
//               <p className="text-xs font-semibold text-[#605E5C] uppercase tracking-wide mb-1">
//                 AI Overall Verdict
//               </p>
//               <p
//                 className="text-2xl font-bold"
//                 style={{ color: overallWinner === "tie" ? "#605E5C" : "#107C10" }}
//               >
//                 {overallWinner === "A"
//                   ? `${nameA} Wins`
//                   : overallWinner === "B"
//                   ? `${nameB} Wins`
//                   : "It's a Tie"}
//               </p>
//               {verdict?.reason && (
//                 <p className="text-sm text-[#323130] mt-1 leading-5">{verdict.reason}</p>
//               )}
//             </div>

//             {/* Score diff pills */}
//             <div className="flex flex-col gap-2 shrink-0">
//               {overallA > 0 && overallB > 0 && (
//                 <div className="bg-white rounded-lg px-4 py-2 text-center shadow-sm">
//                   <p className="text-xs text-[#605E5C]">Score Diff</p>
//                   <p className="text-xl font-bold text-[#323130]">
//                     {Math.abs(overallA - overallB).toFixed(0)} pts
//                   </p>
//                 </div>
//               )}
//               {verdict?.investment_preference && (
//                 <div className="bg-[#E5F1FB] rounded-lg px-4 py-2 text-center">
//                   <p className="text-xs text-[#605E5C]">Investment Preference</p>
//                   <p className="text-sm font-bold text-[#0078D4]">{verdict.investment_preference}</p>
//                 </div>
//               )}
//             </div>
//           </div>

//           {/* ── AI Verdict Details ── */}
//           {verdict && (
//             <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all">
//               <h3 className="text-lg font-bold text-[#323130] mb-4 flex items-center gap-2">
//                 <span>🤖</span> AI Verdict
//               </h3>
//               <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

//                 {/* Startup A strengths */}
//                 {arr(verdict.startup_a_strengths).length > 0 && (
//                   <div>
//                     <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-2">
//                       {nameA} — Strengths
//                     </p>
//                     <ul className="space-y-1">
//                       {arr(verdict.startup_a_strengths).map((s, i) => (
//                         <li key={i} className="flex items-start gap-2 text-sm text-[#323130]">
//                           <span className="text-[#0078D4] shrink-0">✓</span>{s}
//                         </li>
//                       ))}
//                     </ul>
//                   </div>
//                 )}

//                 {/* Startup B strengths */}
//                 {arr(verdict.startup_b_strengths).length > 0 && (
//                   <div>
//                     <p className="text-xs font-semibold text-[#107C10] uppercase tracking-wide mb-2">
//                       {nameB} — Strengths
//                     </p>
//                     <ul className="space-y-1">
//                       {arr(verdict.startup_b_strengths).map((s, i) => (
//                         <li key={i} className="flex items-start gap-2 text-sm text-[#323130]">
//                           <span className="text-[#107C10] shrink-0">✓</span>{s}
//                         </li>
//                       ))}
//                     </ul>
//                   </div>
//                 )}

//                 {/* AI Recommendation */}
//                 {verdict.recommendation && (
//                   <div className="md:col-span-2 bg-[#E5F1FB] rounded-xl p-4">
//                     <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-1">
//                       AI Recommendation
//                     </p>
//                     <p className="text-sm text-[#323130] leading-6">{verdict.recommendation}</p>
//                   </div>
//                 )}
//               </div>
//             </div>
//           )}

//           {/* ── Overview Comparison ── */}
//           <SectionCard icon="📊" title="Comparison Overview">
//             <div className="overflow-x-auto">
//               <table className="w-full">
//                 <TableHeader nameA={nameA} idA={report1} nameB={nameB} idB={report2} />
//                 <tbody>
//                   <CompareRow
//                     label="Overall Score"
//                     valueA={val(reportA.overview?.overall_score ?? reportA.investor?.overall_score)}
//                     valueB={val(reportB.overview?.overall_score ?? reportB.investor?.overall_score)}
//                     winner={numWinner(
//                       reportA.overview?.overall_score ?? reportA.investor?.overall_score,
//                       reportB.overview?.overall_score ?? reportB.investor?.overall_score
//                     )}
//                     isScore scoreA={overallA} scoreB={overallB}
//                   />
//                   <CompareRow
//                     label="Investment Readiness"
//                     valueA={val(reportA.investor?.readiness_score)}
//                     valueB={val(reportB.investor?.readiness_score)}
//                     winner={numWinner(reportA.investor?.readiness_score, reportB.investor?.readiness_score)}
//                     isScore scoreA={readyA} scoreB={readyB}
//                   />
//                   <CompareRow
//                     label="AI Confidence"
//                     valueA={confA > 0 ? `${confA}%` : "N/A"}
//                     valueB={confB > 0 ? `${confB}%` : "N/A"}
//                     winner={numWinner(
//                       reportA.overview?.ai_confidence ?? reportA.investor?.ai_confidence,
//                       reportB.overview?.ai_confidence ?? reportB.investor?.ai_confidence
//                     )}
//                     isScore scoreA={confA} scoreB={confB}
//                   />
//                   <CompareRow
//                     label="Investment Outlook"
//                     valueA={val(reportA.investor?.investment_outlook)}
//                     valueB={val(reportB.investor?.investment_outlook)}
//                     winner="tie"
//                   />
//                   <CompareRow
//                     label="Funding Stage"
//                     valueA={val(reportA.investor?.funding_stage)}
//                     valueB={val(reportB.investor?.funding_stage)}
//                     winner="tie"
//                   />
//                   <CompareRow
//                     label="Recommended Raise"
//                     valueA={val(reportA.investor?.recommended_raise ?? reportA.investor?.raise_amount)}
//                     valueB={val(reportB.investor?.recommended_raise ?? reportB.investor?.raise_amount)}
//                     winner="tie"
//                   />
//                   <CompareRow
//                     label="Risk Level"
//                     valueA={val(reportA.investor?.risk_level)}
//                     valueB={val(reportB.investor?.risk_level)}
//                     winner="tie"
//                   />
//                 </tbody>
//               </table>
//             </div>
//           </SectionCard>

//           {/* ── Market Comparison ── */}
//           <SectionCard icon="🌍" title="Market Comparison">
//             <div className="overflow-x-auto">
//               <table className="w-full">
//                 <TableHeader nameA={nameA} idA={report1} nameB={nameB} idB={report2} />
//                 <tbody>
//                   <CompareRow label="Market Size"  valueA={val(reportA.market?.market_size)}  valueB={val(reportB.market?.market_size)}  winner="tie" />
//                   <CompareRow label="Growth Rate"  valueA={val(reportA.market?.growth_rate)}  valueB={val(reportB.market?.growth_rate)}  winner="tie" />
//                   <CompareRow label="TAM"          valueA={val(reportA.market?.tam)}           valueB={val(reportB.market?.tam)}           winner="tie" />
//                   <CompareRow label="SAM"          valueA={val(reportA.market?.sam)}           valueB={val(reportB.market?.sam)}           winner="tie" />
//                   <CompareRow label="SOM"          valueA={val(reportA.market?.som)}           valueB={val(reportB.market?.som)}           winner="tie" />
//                   <ListCompareRow
//                     label="Opportunities"
//                     itemsA={arr(reportA.market?.opportunities)}
//                     itemsB={arr(reportB.market?.opportunities)}
//                   />
//                 </tbody>
//               </table>
//             </div>
//           </SectionCard>

//           {/* ── Business Comparison ── */}
//           <SectionCard icon="🏢" title="Business Comparison">
//             <div className="overflow-x-auto">
//               <table className="w-full">
//                 <TableHeader nameA={nameA} idA={report1} nameB={nameB} idB={report2} />
//                 <tbody>
//                   <CompareRow label="Business Model"    valueA={val(reportA.business?.business_model)}  valueB={val(reportB.business?.business_model)}  winner="tie" />
//                   <CompareRow label="Target Customer"   valueA={val(reportA.business?.target_customer)} valueB={val(reportB.business?.target_customer)} winner="tie" />
//                   <CompareRow label="Pricing Strategy"  valueA={val(reportA.business?.pricing_strategy)}valueB={val(reportB.business?.pricing_strategy)}winner="tie" />
//                   <CompareRow label="Go-To-Market"      valueA={val(reportA.business?.go_to_market)}    valueB={val(reportB.business?.go_to_market)}    winner="tie" />
//                   <ListCompareRow
//                     label="Revenue Streams"
//                     itemsA={arr(reportA.business?.revenue_streams)}
//                     itemsB={arr(reportB.business?.revenue_streams)}
//                   />
//                 </tbody>
//               </table>
//             </div>
//           </SectionCard>

//           {/* ── SWOT Comparison ── */}
//           <SectionCard icon="🔲" title="SWOT Comparison">
//             <div className="overflow-x-auto">
//               <table className="w-full">
//                 <TableHeader nameA={nameA} idA={report1} nameB={nameB} idB={report2} />
//                 <tbody>
//                   <ListCompareRow label="💪 Strengths"     itemsA={arr(reportA.business?.strengths)}    itemsB={arr(reportB.business?.strengths)} />
//                   <ListCompareRow label="⚠️ Weaknesses"    itemsA={arr(reportA.business?.weaknesses)}   itemsB={arr(reportB.business?.weaknesses)} />
//                   <ListCompareRow label="🚀 Opportunities" itemsA={arr(reportA.business?.opportunities)} itemsB={arr(reportB.business?.opportunities)} />
//                   <ListCompareRow label="🛑 Threats"       itemsA={arr(reportA.business?.threats)}      itemsB={arr(reportB.business?.threats)} />
//                 </tbody>
//               </table>
//             </div>
//           </SectionCard>

//           {/* ── Risk Comparison ── */}
//           <SectionCard icon="⚠️" title="Risk Comparison">
//             <div className="overflow-x-auto">
//               <table className="w-full">
//                 <TableHeader nameA={nameA} idA={report1} nameB={nameB} idB={report2} />
//                 <tbody>
//                   <ListCompareRow label="Business Risks"    itemsA={arr(reportA.investor?.risks)}              itemsB={arr(reportB.investor?.risks)} />
//                   <ListCompareRow label="Market Risks"      itemsA={arr(reportA.investor?.market_risks)}       itemsB={arr(reportB.investor?.market_risks)} />
//                   <ListCompareRow label="Technology Risks"  itemsA={arr(reportA.investor?.technology_risks)}   itemsB={arr(reportB.investor?.technology_risks)} />
//                   <ListCompareRow label="Execution Risks"   itemsA={arr(reportA.investor?.operational_risks)}  itemsB={arr(reportB.investor?.operational_risks)} />
//                 </tbody>
//               </table>
//             </div>
//           </SectionCard>

//           {/* ── Footer Branding ── */}
//           <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-2 border-t border-gray-200">
//             <p className="text-xs text-[#605E5C]">
//               Powered by{" "}
//               <span className="font-semibold text-[#0078D4]">Microsoft Azure AI Foundry</span>{" "}
//               · Comparison Agent
//             </p>
//             {dateA && dateB && (
//               <p className="text-xs text-[#605E5C]">
//                 {nameA}: {dateA} · {nameB}: {dateB}
//               </p>
//             )}
//           </div>

//         </div>
//       )}

//     </div>
//   );
// }

// Fixed Code

"use client";

import { useState } from "react";
import { compareReports } from "@/services/api";

// ── TypeScript Interfaces ──────────────────────────────────────────────────────

interface HistoryItem {
  id: number;
  created_at?: string;
  startup_name?: string;
  report_json?: ReportJson;
}

interface ReportJson {
  market?: {
    market_size?: string;
    growth_rate?: string;
    tam?: string;
    sam?: string;
    som?: string;
    opportunities?: string[];
  };
  business?: {
    business_model?: string;
    target_customer?: string;
    revenue_streams?: string[];
    pricing_strategy?: string;
    go_to_market?: string;
  };
  investor?: {
    readiness_score?: string | number;
    funding_stage?: string;
    recommended_raise?: string;
    raise_amount?: string;
    risks?: string[];
  };
  swot?: {
    strengths?: string[];
    weaknesses?: string[];
    opportunities?: string[];
    threats?: string[];
  };
  analysis_summary?: {
    overall_score?: string | number;
    investment_outlook?: string;
    risk_level?: string;
  };
}

interface ComparisonResult {
  report1?: {
    id?: number;
    report_json?: ReportJson;
    startup_name?: string;
    created_at?: string;
  };
  report2?: {
    id?: number;
    report_json?: ReportJson;
    startup_name?: string;
    created_at?: string;
  };
  ai_verdict?: {
    winner?: string;
    reason?: string;
    startup_a_strengths?: string[];
    startup_b_strengths?: string[];
    recommendation?: string;
    investment_preference?: string;
  };
}

interface Props {
  history?: HistoryItem[];
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function val(v: string | number | undefined, fallback = "N/A"): string {
  return v !== undefined && v !== null && String(v).trim() !== ""
    ? String(v)
    : fallback;
}

function toNum(v: string | number | undefined): number {
  const n = parseFloat(String(v ?? ""));
  return isNaN(n) ? 0 : n;
}

function arr(v: string[] | undefined): string[] {
  return Array.isArray(v) ? v : [];
}

function fmtDate(d: string | undefined): string {
  if (!d) return "";
  try {
    return new Date(d).toLocaleDateString("en-US", { dateStyle: "medium" });
  } catch {
    return d;
  }
}

// Score-based comparison — returns which side "wins" for a numeric metric
function numWinner(a: string | number | undefined, b: string | number | undefined): "A" | "B" | "tie" {
  const na = toNum(a), nb = toNum(b);
  if (na === 0 && nb === 0) return "tie";
  if (na > nb) return "A";
  if (nb > na) return "B";
  return "tie";
}

function scoreColor(v: string | number | undefined, fallback = "#605E5C"): string {
  const n = toNum(v);
  if (n === 0) return fallback;
  if (n >= 75) return "#107C10";
  if (n >= 50) return "#FF8C00";
  return "#D13438";
}

function scoreBg(v: string | number | undefined): string {
  const n = toNum(v);
  if (n === 0) return "#F3F2F1";
  if (n >= 75) return "#DFF6DD";
  if (n >= 50) return "#FFF4CE";
  return "#FDE7E9";
}

function riskColor(level: string | undefined): string {
  const l = (level ?? "").toLowerCase();
  if (l.includes("low"))    return "#107C10";
  if (l.includes("medium")) return "#FF8C00";
  if (l.includes("high"))   return "#D13438";
  return "#605E5C";
}

// ── Reusable Components ───────────────────────────────────────────────────────

function SectionCard({
  icon,
  title,
  children,
}: {
  icon: string;
  title: string;
  children: React.ReactNode;
}) {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-all duration-200">
      <div className="bg-[#F3F2F1] border-b border-gray-200 px-6 py-4 flex items-center gap-2">
        <span className="text-lg">{icon}</span>
        <h3 className="text-base font-bold text-[#323130]">{title}</h3>
      </div>
      <div className="p-0">{children}</div>
    </div>
  );
}

// Side A = blue, Side B = green — winner gets bold highlight
function CompareRow({
  label,
  valueA,
  valueB,
  winner,
  isScore = false,
  scoreA,
  scoreB,
}: {
  label: string;
  valueA: string;
  valueB: string;
  winner: "A" | "B" | "tie";
  isScore?: boolean;
  scoreA?: number;
  scoreB?: number;
}) {
  const cellBase = "p-4 text-center text-sm align-top";
  const winStyle = "font-bold text-[#107C10]";
  const loseStyle = "text-[#605E5C]";
  const tieStyle = "text-[#323130]";

  return (
    <tr className="border-b border-gray-100 hover:bg-[#F9F9F9] transition-colors">
      <td className="p-4 text-sm font-semibold text-[#323130] align-top w-1/4">
        {label}
      </td>
      <td className={`${cellBase} ${winner === "A" ? winStyle : winner === "B" ? loseStyle : tieStyle}`}>
        <div className="flex flex-col items-center gap-1">
          {winner === "A" && (
            <span className="text-xs bg-[#DFF6DD] text-[#107C10] px-2 py-0.5 rounded-full font-semibold mb-1">
              ▲ Stronger
            </span>
          )}
          {winner === "B" && (
            <span className="text-xs bg-[#FDE7E9] text-[#D13438] px-2 py-0.5 rounded-full font-semibold mb-1">
              ▼ Weaker
            </span>
          )}
          <span>{valueA}</span>
          {isScore && scoreA !== undefined && scoreA > 0 && (
            <div className="w-20 bg-gray-100 rounded-full h-1.5 mt-1">
              <div
                className="h-1.5 rounded-full"
                style={{ width: `${Math.min(scoreA, 100)}%`, backgroundColor: scoreColor(scoreA) }}
              />
            </div>
          )}
        </div>
      </td>
      <td className={`${cellBase} ${winner === "B" ? winStyle : winner === "A" ? loseStyle : tieStyle}`}>
        <div className="flex flex-col items-center gap-1">
          {winner === "B" && (
            <span className="text-xs bg-[#DFF6DD] text-[#107C10] px-2 py-0.5 rounded-full font-semibold mb-1">
              ▲ Stronger
            </span>
          )}
          {winner === "A" && (
            <span className="text-xs bg-[#FDE7E9] text-[#D13438] px-2 py-0.5 rounded-full font-semibold mb-1">
              ▼ Weaker
            </span>
          )}
          <span>{valueB}</span>
          {isScore && scoreB !== undefined && scoreB > 0 && (
            <div className="w-20 bg-gray-100 rounded-full h-1.5 mt-1">
              <div
                className="h-1.5 rounded-full"
                style={{ width: `${Math.min(scoreB, 100)}%`, backgroundColor: scoreColor(scoreB) }}
              />
            </div>
          )}
        </div>
      </td>
    </tr>
  );
}

function ListCompareRow({
  label,
  itemsA,
  itemsB,
}: {
  label: string;
  itemsA: string[];
  itemsB: string[];
}) {
  return (
    <tr className="border-b border-gray-100 hover:bg-[#F9F9F9] transition-colors">
      <td className="p-4 text-sm font-semibold text-[#323130] align-top w-1/4">{label}</td>
      <td className="p-4 align-top">
        {itemsA.length > 0 ? (
          <ul className="space-y-1">
            {itemsA.slice(0, 3).map((item, i) => (
              <li key={i} className="flex items-start gap-1.5 text-xs text-[#323130]">
                <span className="text-[#0078D4] shrink-0 mt-0.5">›</span>
                {item}
              </li>
            ))}
            {itemsA.length > 3 && (
              <li className="text-xs text-[#605E5C]">+{itemsA.length - 3} more</li>
            )}
          </ul>
        ) : (
          <span className="text-xs text-[#605E5C]">N/A</span>
        )}
      </td>
      <td className="p-4 align-top">
        {itemsB.length > 0 ? (
          <ul className="space-y-1">
            {itemsB.slice(0, 3).map((item, i) => (
              <li key={i} className="flex items-start gap-1.5 text-xs text-[#323130]">
                <span className="text-[#107C10] shrink-0 mt-0.5">›</span>
                {item}
              </li>
            ))}
            {itemsB.length > 3 && (
              <li className="text-xs text-[#605E5C]">+{itemsB.length - 3} more</li>
            )}
          </ul>
        ) : (
          <span className="text-xs text-[#605E5C]">N/A</span>
        )}
      </td>
    </tr>
  );
}

function TableHeader({
  nameA,
  idA,
  nameB,
  idB,
}: {
  nameA: string;
  idA: string;
  nameB: string;
  idB: string;
}) {
  return (
    <thead>
      <tr>
        <th className="p-4 text-left text-sm font-semibold text-[#605E5C] bg-[#F3F2F1] w-1/4">
          Metric
        </th>
        <th className="p-4 text-center bg-[#E5F1FB] border-b-4 border-[#0078D4]">
          <div className="flex flex-col items-center gap-1">
            <span className="text-lg">🅰️</span>
            <span className="text-sm font-bold text-[#0078D4]">{nameA}</span>
            <span className="text-xs text-[#605E5C]">Report #{idA}</span>
          </div>
        </th>
        <th className="p-4 text-center bg-[#DFF6DD] border-b-4 border-[#107C10]">
          <div className="flex flex-col items-center gap-1">
            <span className="text-lg">🅱️</span>
            <span className="text-sm font-bold text-[#107C10]">{nameB}</span>
            <span className="text-xs text-[#605E5C]">Report #{idB}</span>
          </div>
        </th>
      </tr>
    </thead>
  );
}

// ── Main Component ────────────────────────────────────────────────────────────

export default function CompareStartups({ history }: Props) {

  const reports = Array.isArray(history) ? history : [];

  const [report1, setReport1] = useState("");
  const [report2, setReport2] = useState("");
  const [comparison, setComparison] = useState<ComparisonResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleCompare() {
    if (!report1 || !report2) {
      setError("Please select two different reports to compare.");
      return;
    }
    if (report1 === report2) {
      setError("Please select two different reports.");
      return;
    }
    setError(null);
    setLoading(true);
    try {
      const result = await compareReports(Number(report1), Number(report2));
      setComparison(result);
    } catch (err) {
      console.error(err);
      setError("Comparison failed. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  const reportA: ReportJson = comparison?.report1?.report_json ?? {};
  const reportB: ReportJson = comparison?.report2?.report_json ?? {};
  const nameA = comparison?.report1?.startup_name ?? `Report #${report1}`;
  const nameB = comparison?.report2?.startup_name ?? `Report #${report2}`;
  const dateA = fmtDate(comparison?.report1?.created_at);
  const dateB = fmtDate(comparison?.report2?.created_at);

  // Scores for winner logic
  const overallA  = toNum(reportA.analysis_summary?.overall_score);
  const overallB  = toNum(reportB.analysis_summary?.overall_score);
  const readyA    = toNum(reportA.investor?.readiness_score);
  const readyB    = toNum(reportB.investor?.readiness_score);

  // Determine overall winner (sum of weighted scores: overall 0-100, readiness 0-10 scaled to 0-100)
  const totalA = overallA * 0.5 + (readyA * 10) * 0.5;
  const totalB = overallB * 0.5 + (readyB * 10) * 0.5;
  const overallWinner =
    totalA > totalB ? "A" : totalB > totalA ? "B" : "tie";

  const verdict = comparison?.ai_verdict;

  // ── No reports guard ──
  if (reports.length === 0) {
    return (
      <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-12 text-center space-y-3">
        <span className="text-5xl">📊</span>
        <p className="text-lg font-semibold text-[#323130]">No reports available</p>
        <p className="text-sm text-[#605E5C]">
          Run at least two startup analyses to unlock the comparison feature.
        </p>
      </div>
    );
  }

  if (reports.length === 1) {
    return (
      <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-12 text-center space-y-3">
        <span className="text-5xl">📊</span>
        <p className="text-lg font-semibold text-[#323130]">Only one report available</p>
        <p className="text-sm text-[#605E5C]">
          Analyze a second startup to compare side by side.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-8">

      {/* ── Header ── */}
      <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-[#323130]">Startup Comparison</h1>
          <p className="text-sm text-[#605E5C] mt-1">
            AI-powered side-by-side analysis ·{" "}
            <span className="text-[#0078D4] font-medium">Comparison Agent</span>
          </p>
        </div>
        <div className="flex flex-col gap-2 items-start sm:items-end">
          <span className="bg-[#E5F1FB] text-[#0078D4] px-4 py-2 rounded-full text-sm font-semibold whitespace-nowrap">
            ✦ Microsoft Azure AI Foundry
          </span>
          <span className="bg-[#DFF6DD] text-[#107C10] px-3 py-1 rounded-full text-xs font-semibold whitespace-nowrap">
            ✓ AI-Generated Comparison
          </span>
        </div>
      </div>

      {/* ── Selection Panel ── */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <h2 className="text-base font-bold text-[#323130] mb-4 flex items-center gap-2">
          <span>🔍</span> Select Startups to Compare
        </h2>

        <div className="flex flex-col sm:flex-row gap-4 items-start sm:items-end flex-wrap">

          {/* Dropdown A */}
          <div className="flex flex-col gap-1">
            <label className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide">
              Startup A
            </label>
            <select
              value={report1}
              onChange={(e) => { setReport1(e.target.value); setError(null); }}
              className="border border-gray-300 rounded-lg px-4 py-3 w-72 text-[#323130] bg-white focus:outline-none focus:border-[#0078D4] focus:ring-1 focus:ring-[#0078D4] transition"
            >
              <option value="">Select Report A</option>
              {reports.map((item) => (
                <option
                  key={item.id}
                  value={item.id}
                  disabled={String(item.id) === report2}
                >
                  {item.startup_name ? `${item.startup_name} (#${item.id})` : `Report #${item.id}`}
                  {item.created_at ? ` · ${fmtDate(item.created_at)}` : ""}
                </option>
              ))}
            </select>
          </div>

          <div className="text-2xl text-[#605E5C] font-bold sm:mb-3">vs</div>

          {/* Dropdown B */}
          <div className="flex flex-col gap-1">
            <label className="text-xs font-semibold text-[#107C10] uppercase tracking-wide">
              Startup B
            </label>
            <select
              value={report2}
              onChange={(e) => { setReport2(e.target.value); setError(null); }}
              className="border border-gray-300 rounded-lg px-4 py-3 w-72 text-[#323130] bg-white focus:outline-none focus:border-[#107C10] focus:ring-1 focus:ring-[#107C10] transition"
            >
              <option value="">Select Report B</option>
              {reports.map((item) => (
                <option
                  key={item.id}
                  value={item.id}
                  disabled={String(item.id) === report1}
                >
                  {item.startup_name ? `${item.startup_name} (#${item.id})` : `Report #${item.id}`}
                  {item.created_at ? ` · ${fmtDate(item.created_at)}` : ""}
                </option>
              ))}
            </select>
          </div>

          <button
            onClick={handleCompare}
            disabled={loading || !report1 || !report2 || report1 === report2}
            className="bg-[#0078D4] hover:bg-[#006CBD] disabled:opacity-50 disabled:cursor-not-allowed text-white px-8 py-3 rounded-lg font-semibold transition-all duration-200 sm:mb-0 flex items-center gap-2"
          >
            {loading ? (
              <>
                <span className="animate-spin">⟳</span> Comparing…
              </>
            ) : (
              <>⚡ Compare</>
            )}
          </button>
        </div>

        {error && (
          <div className="mt-4 bg-[#FDE7E9] border border-[#D13438] text-[#D13438] rounded-lg px-4 py-3 text-sm font-medium">
            ⚠️ {error}
          </div>
        )}
      </div>

      {/* ── Results ── */}
      {comparison && (
        <div className="space-y-6">

          {/* ── Winner Banner ── */}
          <div
            className="rounded-xl p-6 border-l-4 flex flex-col sm:flex-row items-start sm:items-center gap-5"
            style={{
              borderColor: overallWinner === "tie" ? "#605E5C" : "#107C10",
              backgroundColor: overallWinner === "tie" ? "#F3F2F1" : "#DFF6DD",
            }}
          >
            <span className="text-5xl shrink-0">
              {overallWinner === "tie" ? "🤝" : "🏆"}
            </span>
            <div className="flex-1">
              <p className="text-xs font-semibold text-[#605E5C] uppercase tracking-wide mb-1">
                AI Overall Verdict
              </p>
              <p
                className="text-2xl font-bold"
                style={{ color: overallWinner === "tie" ? "#605E5C" : "#107C10" }}
              >
                {overallWinner === "A"
                  ? `${nameA} Wins`
                  : overallWinner === "B"
                  ? `${nameB} Wins`
                  : "It's a Tie"}
              </p>
              {verdict?.reason && (
                <p className="text-sm text-[#323130] mt-1 leading-5">{verdict.reason}</p>
              )}
            </div>

            {/* Score diff pills */}
            <div className="flex flex-col gap-2 shrink-0">
              {overallA > 0 && overallB > 0 && (
                <div className="bg-white rounded-lg px-4 py-2 text-center shadow-sm">
                  <p className="text-xs text-[#605E5C]">Score Diff</p>
                  <p className="text-xl font-bold text-[#323130]">
                    {Math.abs(overallA - overallB).toFixed(0)} pts
                  </p>
                </div>
              )}
              {verdict?.investment_preference && (
                <div className="bg-[#E5F1FB] rounded-lg px-4 py-2 text-center">
                  <p className="text-xs text-[#605E5C]">Investment Preference</p>
                  <p className="text-sm font-bold text-[#0078D4]">{verdict.investment_preference}</p>
                </div>
              )}
            </div>
          </div>

          {/* ── AI Verdict Details ── */}
          {verdict && (
            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all">
              <h3 className="text-lg font-bold text-[#323130] mb-4 flex items-center gap-2">
                <span>🤖</span> AI Verdict
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                {/* Startup A strengths */}
                {arr(verdict.startup_a_strengths).length > 0 && (
                  <div>
                    <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-2">
                      {nameA} — Strengths
                    </p>
                    <ul className="space-y-1">
                      {arr(verdict.startup_a_strengths).map((s, i) => (
                        <li key={i} className="flex items-start gap-2 text-sm text-[#323130]">
                          <span className="text-[#0078D4] shrink-0">✓</span>{s}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Startup B strengths */}
                {arr(verdict.startup_b_strengths).length > 0 && (
                  <div>
                    <p className="text-xs font-semibold text-[#107C10] uppercase tracking-wide mb-2">
                      {nameB} — Strengths
                    </p>
                    <ul className="space-y-1">
                      {arr(verdict.startup_b_strengths).map((s, i) => (
                        <li key={i} className="flex items-start gap-2 text-sm text-[#323130]">
                          <span className="text-[#107C10] shrink-0">✓</span>{s}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* AI Recommendation */}
                {verdict.recommendation && (
                  <div className="md:col-span-2 bg-[#E5F1FB] rounded-xl p-4">
                    <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-1">
                      AI Recommendation
                    </p>
                    <p className="text-sm text-[#323130] leading-6">{verdict.recommendation}</p>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* ── Overview Comparison ── */}
          <SectionCard icon="📊" title="Comparison Overview">
            <div className="overflow-x-auto">
              <table className="w-full">
                <TableHeader nameA={nameA} idA={report1} nameB={nameB} idB={report2} />
                <tbody>
                  <CompareRow
                    label="Overall Score"
                    valueA={overallA > 0 ? `${overallA}/100` : "N/A"}
                    valueB={overallB > 0 ? `${overallB}/100` : "N/A"}
                    winner={numWinner(reportA.analysis_summary?.overall_score, reportB.analysis_summary?.overall_score)}
                    isScore scoreA={overallA} scoreB={overallB}
                  />
                  <CompareRow
                    label="Investment Readiness"
                    valueA={readyA > 0 ? `${readyA}/10` : "N/A"}
                    valueB={readyB > 0 ? `${readyB}/10` : "N/A"}
                    winner={numWinner(reportA.investor?.readiness_score, reportB.investor?.readiness_score)}
                    isScore scoreA={readyA * 10} scoreB={readyB * 10}
                  />
                  <CompareRow
                    label="Investment Outlook"
                    valueA={val(reportA.analysis_summary?.investment_outlook)}
                    valueB={val(reportB.analysis_summary?.investment_outlook)}
                    winner="tie"
                  />
                  <CompareRow
                    label="Funding Stage"
                    valueA={val(reportA.investor?.funding_stage)}
                    valueB={val(reportB.investor?.funding_stage)}
                    winner="tie"
                  />
                  <CompareRow
                    label="Recommended Raise"
                    valueA={val(reportA.investor?.recommended_raise ?? reportA.investor?.raise_amount)}
                    valueB={val(reportB.investor?.recommended_raise ?? reportB.investor?.raise_amount)}
                    winner="tie"
                  />
                  <CompareRow
                    label="Risk Level"
                    valueA={val(reportA.analysis_summary?.risk_level)}
                    valueB={val(reportB.analysis_summary?.risk_level)}
                    winner="tie"
                  />
                </tbody>
              </table>
            </div>
          </SectionCard>

          {/* ── Market Comparison ── */}
          <SectionCard icon="🌍" title="Market Comparison">
            <div className="overflow-x-auto">
              <table className="w-full">
                <TableHeader nameA={nameA} idA={report1} nameB={nameB} idB={report2} />
                <tbody>
                  <CompareRow label="Market Size"  valueA={val(reportA.market?.market_size)}  valueB={val(reportB.market?.market_size)}  winner="tie" />
                  <CompareRow label="Growth Rate"  valueA={val(reportA.market?.growth_rate)}  valueB={val(reportB.market?.growth_rate)}  winner="tie" />
                  <CompareRow label="TAM"          valueA={val(reportA.market?.tam)}           valueB={val(reportB.market?.tam)}           winner="tie" />
                  <CompareRow label="SAM"          valueA={val(reportA.market?.sam)}           valueB={val(reportB.market?.sam)}           winner="tie" />
                  <CompareRow label="SOM"          valueA={val(reportA.market?.som)}           valueB={val(reportB.market?.som)}           winner="tie" />
                  <ListCompareRow
                    label="Opportunities"
                    itemsA={arr(reportA.market?.opportunities)}
                    itemsB={arr(reportB.market?.opportunities)}
                  />
                </tbody>
              </table>
            </div>
          </SectionCard>

          {/* ── Business Comparison ── */}
          <SectionCard icon="🏢" title="Business Comparison">
            <div className="overflow-x-auto">
              <table className="w-full">
                <TableHeader nameA={nameA} idA={report1} nameB={nameB} idB={report2} />
                <tbody>
                  <CompareRow label="Business Model"    valueA={val(reportA.business?.business_model)}  valueB={val(reportB.business?.business_model)}  winner="tie" />
                  <CompareRow label="Target Customer"   valueA={val(reportA.business?.target_customer)} valueB={val(reportB.business?.target_customer)} winner="tie" />
                  <CompareRow label="Pricing Strategy"  valueA={val(reportA.business?.pricing_strategy)}valueB={val(reportB.business?.pricing_strategy)}winner="tie" />
                  <CompareRow label="Go-To-Market"      valueA={val(reportA.business?.go_to_market)}    valueB={val(reportB.business?.go_to_market)}    winner="tie" />
                  <ListCompareRow
                    label="Revenue Streams"
                    itemsA={arr(reportA.business?.revenue_streams)}
                    itemsB={arr(reportB.business?.revenue_streams)}
                  />
                </tbody>
              </table>
            </div>
          </SectionCard>

          {/* ── SWOT Comparison ── */}
          <SectionCard icon="🔲" title="SWOT Comparison">
            <div className="overflow-x-auto">
              <table className="w-full">
                <TableHeader nameA={nameA} idA={report1} nameB={nameB} idB={report2} />
                <tbody>
                  <ListCompareRow label="💪 Strengths"     itemsA={arr(reportA.swot?.strengths)}     itemsB={arr(reportB.swot?.strengths)} />
                  <ListCompareRow label="⚠️ Weaknesses"    itemsA={arr(reportA.swot?.weaknesses)}    itemsB={arr(reportB.swot?.weaknesses)} />
                  <ListCompareRow label="🚀 Opportunities" itemsA={arr(reportA.swot?.opportunities)} itemsB={arr(reportB.swot?.opportunities)} />
                  <ListCompareRow label="🛑 Threats"       itemsA={arr(reportA.swot?.threats)}       itemsB={arr(reportB.swot?.threats)} />
                </tbody>
              </table>
            </div>
          </SectionCard>

          {/* ── Risk Comparison ── */}
          <SectionCard icon="⚠️" title="Risk Comparison">
            <div className="overflow-x-auto">
              <table className="w-full">
                <TableHeader nameA={nameA} idA={report1} nameB={nameB} idB={report2} />
                <tbody>
                  <ListCompareRow label="Investment Risks" itemsA={arr(reportA.investor?.risks)} itemsB={arr(reportB.investor?.risks)} />
                  <ListCompareRow label="Market Threats"   itemsA={arr(reportA.swot?.threats)}   itemsB={arr(reportB.swot?.threats)} />
                </tbody>
              </table>
            </div>
          </SectionCard>

          {/* ── Footer Branding ── */}
          <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-2 border-t border-gray-200">
            <p className="text-xs text-[#605E5C]">
              Powered by{" "}
              <span className="font-semibold text-[#0078D4]">Microsoft Azure AI Foundry</span>{" "}
              · Comparison Agent
            </p>
            {dateA && dateB && (
              <p className="text-xs text-[#605E5C]">
                {nameA}: {dateA} · {nameB}: {dateB}
              </p>
            )}
          </div>

        </div>
      )}

    </div>
  );
}

