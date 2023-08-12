app/src/theme/index.ts
======================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import type { Theme } from "@mui/material/styles";
import { lensPath, set, view } from "ramda";

import getOverrides from "./overrides";

export const components = (theme: Theme) => {
  const lens = lensPath(["components"]);
  return set(lens, view(lens, getOverrides(theme)), theme);
};

export const palette = (section: string) => (theme: Theme) => {
  const lens = lensPath(["palette", section]);
  return set(lens, view(lens, getOverrides(theme)), theme);
};


