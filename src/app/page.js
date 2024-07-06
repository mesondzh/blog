import { allPosts } from "contentlayer/generated";
import { compareDesc } from "date-fns";
import Link from "next/link";
import Image from "next/image";
import siteMetadata from "../../data/sitemetadata";
import PostCard from "../components/postcard";

export default function Home() {
  const posts = allPosts.sort((a, b) => {
    return compareDesc(new Date(a.publishDate), new Date(b.publishDate));
  });
  const postsNum = posts.length;
  const totalWords = posts
    .map((post) => post.readingTime.words)
    .reduce((partialSum, a) => partialSum + a, 0)
    .toLocaleString();

  return (
    <div>
      <div className="mx-auto max-w-screen-sm py-2 max-h-screen mt-2">
        <Image
            src={siteMetadata.cover}
            alt='Avatar'
            width="0"
            height="0"
            sizes="100vw"
            style={{ width: '100%', height: 'auto'}}>
        </Image>
      </div>

      <div className="relative lg:grid lg:grid-cols-9 lg:gap-8 pt-0 max-w-6xl">
        <div className="max-w-4xl mx-auto col-span-7">
          <h2 className="pt-16 prose-h2 font-semibold">Featured</h2>
          <div className="py-4 mb-2 md:grid md:grid-cols-2 md:gap-4 lg:gap-8">
            {posts
              .filter((post) => post.draft === false && post.featured == true)
              .slice(0, 4)
              .map((post) => (
                <article key={post._id} className="">
                  <div className="leading-relaxed mx-auto max-w-sm">
                    <PostCard
                      title={post.title}
                      slug={post.slug}
                      description={post.description}
                      publishDate={post.publishDate}
                      readingTime={post.readingTime.text}
                      tags={post.tags}
                      image={post.image}
                    />
                  </div>
                </article>
              ))}
          </div>
          <h2 className="font-semibold prose-h2 pt-4">Latest</h2>
          <div className="md:grid md:grid-cols-2 md:gap-8 lg:gap-12">
            {posts
              .filter((post) => post.draft === false && post.featured !== true)
              .slice(0, 10)
              .map((post) => (
                <article key={post._id} className="">
                  <div className="leading-relaxed mx-auto max-w-sm">
                    <PostCard
                      title={post.title}
                      slug={post.slug}
                      description={post.description}
                      publishDate={post.publishDate}
                      readingTime={post.readingTime.text}
                      tags={post.tags}
                    />
                  </div>
                </article>
              ))}
          </div>
          <Link href="archive">
            <p className="text-right text-sm text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 hover:underline transition duration-400">
              Read More →
            </p>
          </Link>
        </div>
        <div className="col-span-2 max-w-lg mx-auto">
          <div className="sticky top-0 pt-12">
            <h2 className="font-semibold prose-h2" style={{ textAlign: 'center' }}>About Author</h2>
            <Link href="/about">
              <Image
                src={siteMetadata.avatar}
                alt="Avatar"
                width="100"
                height="100"
                className="rounded-full max-w-md mx-auto drop-shadow mt-6 hover:shadow hover:ring-1 hover:ring-zinc-100 dark:ring-zinc-500 transition transform duration-500"
              />
            </Link>
            <p className="prose-lg text-center pt-4">{siteMetadata.author}</p>

            <div className="grid grid-cols-2 divide-x dark:divide-zinc-700 py-4 mx-auto">
              <div className="grid grid-rows-2  text-center px-2">
                <Link
                  href="/blog"
                  className="hover:underline hover:underline-offset-2"
                >
                  {postsNum}
                </Link>
                <p className="text-sm text-zinc-600 dark:text-zinc-400 pt-1">
                  Posts
                </p>
              </div>

              <div className="grid grid-rows-2  text-center px-2">
                {totalWords}
                <p className="text-sm text-zinc-600 dark:text-zinc-400 pt-1">
                  Words
                </p>
              </div>
            </div>
            <p className="py-4 text-center mx-auto prose-p">
              {siteMetadata.authorDesc}
            </p>
            <Link href="/about" passHref>
              <p className="text-right text-sm pt-2 text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 hover:underline transition duration-400">
                About More →
              </p>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export const metadata = {
  title: siteMetadata.title,
  description: siteMetadata.description,
  openGraph: {
    title: siteMetadata.title,
    description: siteMetadata.description,
    url: siteMetadata.siteUrl,
    images: [siteMetadata.cover],
    authors: [siteMetadata.author],
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: siteMetadata.title,
    description: siteMetadata.description,
    siteId: siteMetadata.twitterId,
    creator: siteMetadata.twitter,
    creatorId: siteMetadata.twitterId,
    images: [siteMetadata.cover],
  },
  locale: siteMetadata.language,
  type: "website",
};
