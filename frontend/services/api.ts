const API_URL =
  process.env.NEXT_PUBLIC_API_URL ||
  "http://127.0.0.1:8000";


export async function uploadFile(
  file: File
) {

  const formData = new FormData();

  formData.append(
    "file",
    file
  );

  const response = await fetch(
    `${API_URL}/upload`,
    {
      method: "POST",
      body: formData,
    }
  );

  return response.json();
}

export async function analyseStartup(path: string) {
  const response = await fetch(`${API_URL}/analyse`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ path }),
  });

  console.log("Status:", response.status);
  console.log("OK:", response.ok);
  console.log("Content-Type:", response.headers.get("content-type"));

  const text = await response.text();
  console.log("Raw Response:", text);

  if (!response.ok) {
    throw new Error(text);
  }

  return JSON.parse(text);
}

export async function getHistory() {

  const response =
    await fetch(
      `${API_URL}/history`
    );

  return response.json();
}

export async function getReport(
  id: number
) {

  const response =
    await fetch(
      `${API_URL}/history/${id}`
    );

  return response.json();
}

export async function compareReports(
  id1: number,
  id2: number
) {

  const response =
    await fetch(
      `${API_URL}/compare/${id1}/${id2}`
    );

  return response.json();
}

export function exportReport(
  reportId: number
) {

  window.open(
    `${API_URL}/export/${reportId}`,
    "_blank"
  );

}