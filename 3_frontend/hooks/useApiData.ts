// Custom hook: fetches JSON data from the backend API and exposes
// loading/error/data state. Centralizes fetch logic so components
// stay presentational.

import { useEffect, useState } from "react";

interface ApiState<T> {
  data: T | null;
  loading: boolean;
  error: string | null;
}

export function useApiData<T>(endpoint: string): ApiState<T> {
  const [state, setState] = useState<ApiState<T>>({
    data: null,
    loading: true,
    error: null,
  });

  useEffect(() => {
    let cancelled = false;

    fetch(`/api${endpoint}`)
      .then((res) => {
        if (!res.ok) throw new Error(`Request failed: ${res.status}`);
        return res.json();
      })
      .then((data) => {
        if (!cancelled) setState({ data, loading: false, error: null });
      })
      .catch((err) => {
        if (!cancelled) setState({ data: null, loading: false, error: err.message });
      });

    // Prevent state updates if the component unmounts mid-request.
    return () => {
      cancelled = true;
    };
  }, [endpoint]);

  return state;
}
