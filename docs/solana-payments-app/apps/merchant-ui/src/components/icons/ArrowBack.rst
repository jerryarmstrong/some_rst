apps/merchant-ui/src/components/icons/ArrowBack.tsx
===================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    type Props = React.SVGAttributes<SVGElement>;

export function ArrowBack(props: Props) {
    return (
        <svg {...props} viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z" />
        </svg>
    );
}


