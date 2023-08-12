tests/rustdoc-js-std/parser-literal.js
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    const QUERY = ['R<P>'];

const PARSED = [
    {
        elems: [{
            name: "r",
            fullPath: ["r"],
            pathWithoutLast: [],
            pathLast: "r",
            generics: [
                {
                    name: "p",
                    fullPath: ["p"],
                    pathWithoutLast: [],
                    pathLast: "p",
                    generics: [],
                },
            ],
        }],
        foundElems: 1,
        original: "R<P>",
        returned: [],
        typeFilter: -1,
        userQuery: "r<p>",
        error: null,
    }
];


