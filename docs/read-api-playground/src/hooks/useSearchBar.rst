src/hooks/useSearchBar.tsx
==========================

Last edited: 2023-01-27 22:22:52

Contents:

.. code-block:: tsx

    import { useState, Dispatch } from "react";

interface ISearchBarResponse {
  results: any;
  error: string | undefined;
}

const useSearchBar = (defaultValue: string | undefined): [string | undefined, Dispatch<any>] => {
  const [searchUrl, setSearchUrl] = useState<string | undefined>(defaultValue);
  return [searchUrl, setSearchUrl];
};

export default useSearchBar;


