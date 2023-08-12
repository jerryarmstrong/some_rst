apps/merchant-ui/src/components/PaginatedTablePageIndicatorButton.tsx
=====================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { twMerge } from 'tailwind-merge';

interface Props extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    selected?: boolean;
}

export function PaginatedTablePageIndicatorButton(props: Props) {
    const { children, className, selected, ...rest } = props;
    return (
        <button
            {...rest}
            className={twMerge(
                'flex',
                'font-medium',
                'h-10',
                'items-center',
                'justify-center',
                'rounded-lg',
                'text-sm',
                'text-slate-500',
                'transition-colors',
                'hover:text-slate-800',
                selected && 'bg-gray-50',
                selected && 'text-slate-800',
                'w-10',
                className,
            )}
        >
            {children}
        </button>
    );
}


