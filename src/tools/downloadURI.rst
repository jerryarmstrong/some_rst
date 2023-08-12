src/tools/downloadURI.ts
========================

Last edited: 2023-05-04 20:47:44

Contents:

.. code-block:: ts

    export default function downloadURI(uri: string, name: string): void {
  const link = document.createElement("a");
  link.download = name;
  link.href = uri;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}


