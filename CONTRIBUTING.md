# Contributing to pyprep

* [Questions and Problems](#questions)
* [Issues and Bugs](#issue)
* [Feature Requests](#feature)
* [Issue Submission Guidelines](#submit)
* [Pull Request Submission Guidelines](#submit-pr)

## <a name="requests"></a> Questions, Bugs, Features

If you find a bug in the source code or would like to request a feature (i.e. cs concept to be included), you can help by submitting an issue to the [GitHub Repository][github].

## <a name="submit"></a> Issue Submission Guidelines

Before you submit your issue search the archive to make sure it's not a duplicate. If your issue appears to be a new bug or feature open an issue.

The "[new issue][github-new-issue]" form contains a number of prompts that you should fill out to make it easier to understand and categorize the issue.

## <a name="submit-pr"></a> Pull Request Submission Guidelines

Before you submit your pull request consider the following guidelines:

* Search [GitHub][github-pulls] for an open or closed Pull Request
  that relates to your submission. You don't want to duplicate effort.
* Create the [development environment][developers.setup]
* Make your changes in a new git branch.
* Create your patch commit, **including appropriate test cases**.
* Follow the [Coding Rules][developers.rules].
* Run [unit][developers.tests-unit] tests, and ensure that all tests pass.
* Commit your changes using a descriptive commit message that follows our
  [commit message conventions][developers.commits].
* Push your branch to GitHub
* In GitHub, open a pull request
* If I suggest changes, then:
  * Make the required updates.
  * Re-run the unit tests to ensure tests are still passing.
  * Amend your commits to your branch.
  * Push the changes to the GitHub repository (this will update your Pull Request).

### After your pull request is merged

After your pull request is merged, you can safely delete your branch and pull the changes from the main (upstream) repository.

[coc]: CODE_OF_CONDUCT.md
[developers]: DEVELOPERS.md
[developers.commits]: DEVELOPERS.md#commits
[developers.documentation]: DEVELOPERS.md#documentation
[developers.rules]: DEVELOPERS.md#rules
[developers.setup]: DEVELOPERS.md#setup
[developers.tests-unit]: DEVELOPERS.md#unit-tests
[github-issues]: https://github.com/hlatourette/study/issues
[github-new-issue]: https://github.com/hlatourette/study/issues/new
[github-pulls]: https://github.com/hlatourette/study/pulls
[github]: https://github.com/hlatourette/study
