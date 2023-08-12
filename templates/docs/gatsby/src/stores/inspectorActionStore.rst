templates/docs/gatsby/src/stores/inspectorActionStore.ts
========================================================

Last edited: 2021-10-02 02:46:04

Contents:

.. code-block:: ts

    import { createStore } from "reusable";
import { useState } from "react";

export default createStore(() => {
  const [inspectorContents, setInspectorContents] = useState();
  return [inspectorContents, setInspectorContents];
});


