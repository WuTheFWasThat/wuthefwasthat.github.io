To install:
- Install ruby
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

rm -rf vimflowy
# cp -r ../vimflowy/static/* vimflowy/
cp -r ../vimflowy-2/build vimflowy
