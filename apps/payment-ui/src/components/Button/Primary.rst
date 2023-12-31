apps/payment-ui/src/components/Button/Primary.tsx
=================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { forwardRef } from 'react';
import { twMerge } from 'tailwind-merge';

interface Props extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    pending?: boolean;
    disabled?: boolean;
}

export const Primary = forwardRef<HTMLButtonElement, Props>(function Primary(props, ref) {
    const { pending, disabled, ...rest } = props;

    return (
        <button
            {...rest}
            ref={ref}
            className={twMerge(
                'bg-indigo-600',
                'flex',
                'group',
                'h-10',
                'items-center',
                'justify-center',
                'px-4',
                'relative',
                'rounded-lg',
                'text-indigo-50',
                'tracking-normal',
                'transition-colors',
                rest.className,
                !pending && 'active:bg-indigo-400',
                'disabled:bg-slate-200',
                'disabled:cursor-not-allowed',
                !pending && 'hover:bg-indigo-500',
                pending && 'cursor-not-allowed',
            )}
            onClick={e => {
                if (!pending && !disabled) {
                    rest.onClick?.(e);
                }
            }}
            disabled={disabled}
        >
            <div
                className={twMerge(
                    'flex',
                    'font-semibold',
                    'items-center',
                    'justify-center',
                    'text-current',
                    'text-sm',
                    'transition-all',
                    'group-disabled:text-neutral-400',
                    pending ? 'opacity-0' : 'opacity-100',
                )}
            >
                {rest.children}
            </div>
            {/* {pending && <LoadingDots className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2" />} */}
            {pending && (
                <span className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 loading loading-spinner loading-sm " />
            )}
        </button>
    );
});


