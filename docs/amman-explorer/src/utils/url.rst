src/utils/url.ts
================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    import { useLocation } from "react-router-dom";
import { Location } from "history";

export function getQuery() {
  return new URLSearchParams(window.location.search);
}

export function useQuery() {
  return new URLSearchParams(useLocation().search);
}

export const clusterPath = (pathname: string, params?: URLSearchParams) => {
  return (location: Location) => ({
    ...pickClusterParams(location, params),
    pathname,
  });
};

export function pickClusterParams(
  location: Location,
  newParams?: URLSearchParams
): Location {
  const urlParams = new URLSearchParams(location.search);
  const cluster = urlParams.get("cluster");
  const customUrl = urlParams.get("customUrl");

  // Pick the params we care about
  newParams = newParams || new URLSearchParams();
  if (cluster) newParams.set("cluster", cluster);
  if (customUrl) newParams.set("customUrl", customUrl);

  return {
    ...location,
    search: newParams.toString(),
  };
}


