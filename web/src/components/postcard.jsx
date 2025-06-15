import React, { useState } from "react";

export default function PostCard({ post }) {
  const [likes, setLikes] = useState(post.likes);
  const [comment, setComment] = useState("");
  const [comments, setComments] = useState(post.comments || []);

  const handleLike = () => setLikes(likes + 1);
  const handleComment = () => {
    if (comment.trim()) {
      setComments([...comments, comment]);
      setComment("");
    }
  };

  return (
    <div className="post-card">
      <img src={post.image} alt="post" />
      <p>
        <strong>{post.username}</strong>
      </p>
      <p>{post.caption}</p>
      <button onClick={handleLike}>❤️ {likes}</button>
      <input
        type="text"
        value={comment}
        placeholder="Add a comment..."
        onChange={(e) => setComment(e.target.value)}
      />
      <button onClick={handleComment}>Post</button>
      <div className="comment-section">
        {comments.map((c, i) => (
          <p key={i}>
            <strong>User:</strong> {c}
          </p>
        ))}
      </div>
    </div>
  );
}
