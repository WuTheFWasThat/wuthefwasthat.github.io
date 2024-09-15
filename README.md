To install:
- Install ruby, has to be 3.2.4 (see https://medium.com/@ritviknag/ruby-versioning-trouble-with-jekyll-github-pages-fd2748bf4e1d and https://www.moncefbelyamani.com/making-github-pages-work-with-latest-jekyll/)
- Install bundler: `gem install bundler`
- `bundle install`

To run locally:
```bundle exec jekyll serve```

# TODO

- change workflow to use _drafts instead of git branches?

to build other sub-sites
cp ../send_a_damned_message/build/* send-a-damned-message/
cp ../bearcat-game/static/* bearcat-game/
cp -r ../teach_us/* teach_us/
cp -r ../vimflowy/build/* vimflowy/
cp -r ../wormhole_gets_the_bird_early/build/* the-wormhole-gets-the-bird-early/
