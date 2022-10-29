# Who Unfollowed Me

## :snake: Python Implementation

<img src="https://github.com/TechWiz-3/who-unfollowed-me/blob/main/media/regular.png?raw=true" width="700px"></img>  

**Check Issues for HacktoberFest**  

**Breaking Change for development in [#34](https://github.com/TechWiz-3/who-unfollowed-me/pull/34)** - please delete the `~/.unfollow/unfollow.toml` file before running `unfollow` again!

### :mirror: About

Python CLI tool that shows you who has unfollowed you on GitHub.  
Heavily inspired by [msaaddev/who-unfollowed-me](https://github.com/msaaddev/who-unfollowed-me)  

### :wrench: Installation

![PyPI - Downloads](https://img.shields.io/pypi/dm/unfollow?style=flat-square&color=blue)

```py
pip install unfollow
```

### :receipt:	Usage

The first time you run the tool, you will be asked to enter your GitHub username. Subsequent runs will show any unfollowers, with names and links.  

I used this project to learn a lot about [rich](https://github.com/Textualize/rich), thus I created numerous themes which you can use.

`unfollow` - colored text and some panels  
`unfollow panels` - colored text inside panels  
`unfollow bubbles` - all text inside beautiful bubbles - requires a nerd font  
`unfollow simple` - no colors or emojis, just plain text and a table - coming soon  

### :slightly_smiling_face:	Inspiration

As mentioned, [msaaddev/who-unfollowed-me](https://github.com/msaaddev/who-unfollowed-me) was the reason I created this project and has been a great reference. While I love the project, three things stood out to me that I wanted to improve in my own implementation:

1. The data files for the tool are not hidden and are stored in your current directory rather than the home directory
2. Output looks good but a huge amount is self promotion rather than actual relevant info. (Please don't get me wrong, everyone can self promote as much as they like, I'm just talking about what I wanted to improve)
3. If the tool is run without internet connection, the file that stores the username is erased

###  :framed_picture:	 Gallery

#### Bubbles (w/nerd font)

<img src="https://github.com/TechWiz-3/who-unfollowed-me/blob/main/media/bubbles.png?raw=true" ></img>

#### :point_down: Panels

<img src="https://github.com/TechWiz-3/who-unfollowed-me/blob/main/media/panels.png?raw=true" ></img>

### :computer: Development 

1. Clone the repo and cd into it:
```
git clone https://github.com/TechWiz-3/who-unfollowed-me.git
cd who-unfollowed-me
```
2. Ensure `poetry` is installed by running:`pip install poetry`
3. Run: `poetry install`
4. Make your changes
5. To test your changes, run: `poetry run unfollow` in project root directory

---

### 🎉 Commit labels

If you're interested in the commit labels used in this repo, check out my [git-commit-emoji](https://github.com/TechWiz-3/git-commit-emojis) project

---

### :trophy: Thanks to all the contributions :hearts:	

<a href="https://github.com/TechWiz-3/who-unfollowed-me/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=TechWiz-3/who-unfollowed-me" />
</a>


Made with [contrib.rocks](https://contrib.rocks).

##### Keep contributing! Happy Coding! :v:	
