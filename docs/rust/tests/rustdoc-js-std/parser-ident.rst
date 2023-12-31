tests/rustdoc-js-std/parser-ident.js
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    const QUERY = [
    "R<!>",
    "!",
    "a!",
    "a!::b",
    "a!::b!",
];

const PARSED = [
    {
        elems: [{
            name: "r",
            fullPath: ["r"],
            pathWithoutLast: [],
            pathLast: "r",
            generics: [
                {
                    name: "!",
                    fullPath: ["!"],
                    pathWithoutLast: [],
                    pathLast: "!",
                    generics: [],
                },
            ],
        }],
        foundElems: 1,
        original: "R<!>",
        returned: [],
        typeFilter: -1,
        userQuery: "r<!>",
        error: null,
    },
    {
        elems: [{
            name: "!",
            fullPath: ["!"],
            pathWithoutLast: [],
            pathLast: "!",
            generics: [],
        }],
        foundElems: 1,
        original: "!",
        returned: [],
        typeFilter: -1,
        userQuery: "!",
        error: null,
    },
    {
        elems: [{
            name: "a!",
            fullPath: ["a!"],
            pathWithoutLast: [],
            pathLast: "a!",
            generics: [],
        }],
        foundElems: 1,
        original: "a!",
        returned: [],
        typeFilter: -1,
        userQuery: "a!",
        error: null,
    },
    {
        elems: [{
            name: "a!::b",
            fullPath: ["a!", "b"],
            pathWithoutLast: ["a!"],
            pathLast: "b",
            generics: [],
        }],
        foundElems: 1,
        original: "a!::b",
        returned: [],
        typeFilter: -1,
        userQuery: "a!::b",
        error: null,
    },
    {
        elems: [{
            name: "a!::b!",
            fullPath: ["a!", "b!"],
            pathWithoutLast: ["a!"],
            pathLast: "b!",
            generics: [],
        }],
        foundElems: 1,
        original: "a!::b!",
        returned: [],
        typeFilter: -1,
        userQuery: "a!::b!",
        error: null,
    },
];


