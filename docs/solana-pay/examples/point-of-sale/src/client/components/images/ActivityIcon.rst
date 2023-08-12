examples/point-of-sale/src/client/components/images/ActivityIcon.tsx
====================================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: tsx

    import React, { FC, SVGProps } from 'react';

export const ActivityIcon: FC<SVGProps<SVGSVGElement>> = ({ width = 20, height = 20 }) => {
    return (
        <svg width={width} height={height} fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path
                d="m13 2-10 12h9l-1 8 10-12h-9z"
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
            />
        </svg>
    );
};


