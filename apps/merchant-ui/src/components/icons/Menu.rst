apps/merchant-ui/src/components/icons/Menu.tsx
==============================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    type Props = React.SVGAttributes<SVGElement>;

export function Menu(props: Props) {
    return (
        <svg {...props} viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z" />{' '}
        </svg>
    );
}


