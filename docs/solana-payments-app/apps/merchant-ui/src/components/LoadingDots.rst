apps/merchant-ui/src/components/LoadingDots.tsx
===============================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { twMerge } from 'tailwind-merge';

interface Props {
    className?: string;
    numDots: number;
    style: 'bounce' | 'pulse';
}

export function LoadingDots(props: Props) {
    return (
        <div className={twMerge(props.className, 'flex', 'items-center', 'justify-center', 'gap-x-[0.25em]')}>
            {Array.from({ length: props.numDots }).map((_, i) => (
                <div
                    className={twMerge(
                        props.style === 'bounce' ? 'animate-staggered-bounce' : 'animate-pulse',
                        'bg-current',
                        'flex-shrink-0',
                        'h-[0.33em]',
                        'rounded-full',
                        'w-[0.33em]',
                    )}
                    key={i}
                    style={{
                        animationDelay: `${i * 200}ms`,
                    }}
                />
            ))}
        </div>
    );
}

LoadingDots.defaultProps = {
    numDots: 3,
    style: 'bounce',
};


