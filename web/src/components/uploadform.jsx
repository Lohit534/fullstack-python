import React, { useState } from "react";

export default function UploadForm({ onPost }) {
  const [caption, setCaption] = useState("");
  const [imageURL, setImageURL] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (caption && imageURL) {
      onPost({
        username: "you",
        caption,
        image: imageURL,
        likes: 0,
        comments: [],
      });
      setCaption("");
      setImageURL("");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white shadow-md p-4 rounded-md">
      <input
        placeholder="Image URL"
        className="border p-2 w-full"
        value={imageURL}
        onChange={(e) => setImageURL(e.target.value)}
      />
      <input
        placeholder="Caption"
        className="border p-2 w-full mt-2"
        value={caption}
        onChange={(e) => setCaption(e.target.value)}
      />
      <button
        className="bg-green-500 text-white px-3 py-1 mt-2 rounded"
        type="submit"
      >
        Upload
      </button>
    </form>
  );
}
