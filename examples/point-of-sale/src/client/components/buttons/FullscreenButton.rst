examples/point-of-sale/src/client/components/buttons/FullscreenButton.tsx
=========================================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: tsx

    import React, { FC } from 'react';
import { useFullscreen } from '../../hooks/useFullscreen';
import { MaximizeIcon } from '../images/MaximizeIcon';
import { MinimizeIcon } from '../images/MinimizeIcon';
import css from './FullscreenButton.module.css';

export const FullscreenButton: FC = () => {
    const { fullscreen, toggleFullscreen } = useFullscreen();

    return (
        <button className={css.button} type="button" onClick={toggleFullscreen}>
            {fullscreen ? <MinimizeIcon /> : <MaximizeIcon />}
        </button>
    );
};


