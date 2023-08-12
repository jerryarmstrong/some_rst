apps/merchant-ui/src/components/PaymentsOverviewItem.tsx
========================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { twMerge } from 'tailwind-merge';

interface Props {
    className?: string;
    title: string;
    value: number;
}

export function PaymentsOverviewItem(props: Props) {
    return (
        <div className={twMerge('drop-shadow-sm', 'border-gray-200', 'border', 'p-6', 'rounded-xl', props.className)}>
            <div className="text-sm font-medium text-slate-600">{props.title}</div>
            <div className="mt-2 text-3xl text-slate-900 font-semibold">{props.value}</div>
        </div>
    );
}


