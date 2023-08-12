apps/merchant-ui/src/components/DefaultLayoutHeader.tsx
=======================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { twMerge } from 'tailwind-merge';

interface Props {
    className?: string;
    children: string;
}

export function DefaultLayoutHeader(props: Props) {
    return <div className={twMerge('font-semibold', 'pb-2', 'text-2xl', props.className)}>{props.children}</div>;
}


