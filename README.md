# RTM Sleep Checker

I use [Remember the Milk](http://rememberthemilk.com) all the time, and this
is an implementation of a feature I've been wanting. I'm using
[Heroku](http://heroku.com) with the
[Scheduler addon](http://addons.heroku.com/scheduler) to run `python check.py`
every night.

The check script gets all tasks due today with certain tags, and unsets their
due dates. I made this because I want to be able to "put off" tasks so they
don't show up until a certain date, but I want them to just be general "do
whenever" after that date. My solution is to remove the due date when it comes.

