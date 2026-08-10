// Landing/home screen. Pulls records from the API via useApiData and
// renders each one inside a Card component.

import { Card } from "../components/Card";
import { useApiData } from "../hooks/useApiData";

interface RecordItem {
  id: string;
  payload: Record<string, unknown>;
}

export default function HomePage() {
  const { data, loading, error } = useApiData<RecordItem[]>("/records");

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <main style={{ padding: 24 }}>
      <h1>my-platform</h1>
      {data?.map((record) => (
        <Card key={record.id} title={record.id}>
          <pre>{JSON.stringify(record.payload, null, 2)}</pre>
        </Card>
      ))}
    </main>
  );
}
