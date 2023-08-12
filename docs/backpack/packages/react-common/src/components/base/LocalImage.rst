packages/react-common/src/components/base/LocalImage.tsx
========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useEffect, useState } from "react";
import { getImage, LocalImageManager } from "@coral-xyz/db";

import { ProxyImage } from "./ProxyImage";

export const LocalImage = (props) => {
  const [imageUrl, setImageUrl] = useState(props.src);

  const fetchData = async (src) => {
    if (src) {
      try {
        const parsedEl = await getImage("images", `image-${src}`);
        if (parsedEl) {
          LocalImageManager.getInstance().addToQueue({
            image: src,
          });
        }
        setImageUrl(parsedEl?.url || src);
      } catch (e) {
        setImageUrl(src);
      }
    }
  };
  useEffect(() => {
    fetchData(props.src);
  }, [props.src]);

  return (
    <ProxyImage
      src={imageUrl}
      onClick={props.onClick}
      alt={props.alt}
      className={props.className}
      style={props.style}
      loadingStyles={props.loadingStyles}
      size={props.size}
    />
  );
};


