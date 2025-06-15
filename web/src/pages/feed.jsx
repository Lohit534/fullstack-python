import React, { useState } from "react";
import PostCard from "../components/postcard";
import UploadForm from "../components/uploadform";
import { v4 as uuidv4 } from "uuid";

export default function Feed() {
  const [posts, setPosts] = useState([]);

  const addNewPost = (post) => {
    setPosts([{ ...post, id: uuidv4() }, ...posts]);
  };

  return (
    <div className="p-4">
      <UploadForm onPost={addNewPost} />
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {posts.map((post) => (
          <PostCard key={post.id} post={post} />
        ))}
      </div>
    </div>
  );
}
