src/tools/toDataUrl.ts
======================

Last edited: 2023-05-04 20:47:44

Contents:

.. code-block:: ts

    export default async function toDataURL(url: string): Promise<string> {
  return new Promise((resolve) => {
    const xhr = new XMLHttpRequest();
    xhr.onload = function () {
      const reader = new FileReader();
      reader.onloadend = function () {
        resolve(reader.result as string);
      };
      reader.readAsDataURL(xhr.response);
    };
    xhr.open("GET", url);
    xhr.responseType = "blob";
    xhr.send();
  });
}


