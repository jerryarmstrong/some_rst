apps/merchant-ui/src/components/RefundCount.tsx
===============================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { twMerge } from 'tailwind-merge';

interface Props {
    className?: string;
    refundCount: number;
}

export function RefundCount(props: Props) {
    return (
        <div
            className={twMerge(
                'bg-indigo-100',
                'font-medium',
                'px-2',
                'py-0.5',
                'rounded-full',
                'text-indigo-600',
                'text-xs',
                props.className,
            )}
        >
            {props.refundCount}
        </div>
    );
}


