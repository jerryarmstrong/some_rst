apps/merchant-ui/src/components/icons/ArrowDropDownCircle.tsx
=============================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    type Props = React.SVGAttributes<SVGElement>;

export function ArrowDropDownCircle(props: Props) {
    return (
        <svg {...props} viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 4c4.41 0 8 3.59 8 8s-3.59 8-8 8-8-3.59-8-8 3.59-8 8-8m0-2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 13l-4-4h8z" />{' '}
        </svg>
    );
}


