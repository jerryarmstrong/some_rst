src/stores/inspectorActionStore.ts
==================================

Last edited: 2023-01-27 22:22:52

Contents:

.. code-block:: ts

    import { createStore } from "reusable";
import { useState } from "react";

export default createStore(() => {
  const [inspectorContents, setInspectorContents] = useState();
  return [inspectorContents, setInspectorContents];
});


