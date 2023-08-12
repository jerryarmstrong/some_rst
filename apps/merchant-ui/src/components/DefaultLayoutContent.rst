apps/merchant-ui/src/components/DefaultLayoutContent.tsx
========================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { twMerge } from 'tailwind-merge';

interface Props {
    className?: string;
    children?: React.ReactNode;
}

export function DefaultLayoutContent(props: Props) {
    return (
        <article className={twMerge('px-4', 'py-8', 'md:pl-16', 'md:pr-24', 'md:pt-32', props.className)}>
            {props.children}
        </article>
    );
}


