tests/rustdoc-js-std/parser-quote.js
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    const QUERY = [
    '-> "p"',
    '"p",',
    '"p" -> a',
    '"a" -> "p"',
    '->"-"',
    '"a',
    '""',
];

const PARSED = [
    {
        elems: [],
        foundElems: 1,
        original: '-> "p"',
        returned: [{
            name: "p",
            fullPath: ["p"],
            pathWithoutLast: [],
            pathLast: "p",
            generics: [],
        }],
        typeFilter: -1,
        userQuery: '-> "p"',
        error: null,
    },
    {
        elems: [{
            name: "p",
            fullPath: ["p"],
            pathWithoutLast: [],
            pathLast: "p",
            generics: [],
        }],
        foundElems: 1,
        original: '"p",',
        returned: [],
        typeFilter: -1,
        userQuery: '"p",',
        error: null,
    },
    {
        elems: [],
        foundElems: 0,
        original: '"p" -> a',
        returned: [],
        typeFilter: -1,
        userQuery: '"p" -> a',
        error: "You cannot have more than one element if you use quotes",
    },
    {
        elems: [],
        foundElems: 0,
        original: '"a" -> "p"',
        returned: [],
        typeFilter: -1,
        userQuery: '"a" -> "p"',
        error: "Cannot have more than one literal search element",
    },
    {
        elems: [],
        foundElems: 0,
        original: '->"-"',
        returned: [],
        typeFilter: -1,
        userQuery: '->"-"',
        error: 'Unexpected `-` in a string element',
    },
    {
        elems: [],
        foundElems: 0,
        original: '"a',
        returned: [],
        typeFilter: -1,
        userQuery: '"a',
        error: 'Unclosed `"`',
    },
    {
        elems: [],
        foundElems: 0,
        original: '""',
        returned: [],
        typeFilter: -1,
        userQuery: '""',
        error: 'Cannot have empty string element',
    },
];


