apps/merchant-ui/src/components/DefaultLayoutScreenTitle.tsx
============================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { twMerge } from 'tailwind-merge';

interface Props {
    className?: string;
    children?: React.ReactNode;
}

export function DefaultLayoutScreenTitle(props: Props) {
    return (
        <h1 className={twMerge('font-semibold', 'text-3xl', 'text-black', 'md:text-5xl', props.className)}>
            {props.children}
        </h1>
    );
}


