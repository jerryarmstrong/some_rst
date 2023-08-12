utils/markdown.js
=================

Last edited: 2022-09-30 13:07:41

Contents:

.. code-block:: js

    import { remark } from "remark";
import remarkGfm from "remark-gfm";
import html from "remark-html";
import prism from "remark-prism";

export default async function markdownToHtml(markdown) {
  const result = await remark()
    .use(remarkGfm)
    .use(html, { sanitize: false })
    .use(prism, {
      transformInlineCode: true,
    })
    .process(markdown);

  return result.toString();
}


