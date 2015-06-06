from jirafs.plugin import (
    #  BlockElementMacroPlugin,
    #  CommandPlugin,
    Plugin as GenericPlugin,
    #  PluginOperationError,
    #  PluginValidationError,
    #  VoidElementMacroPlugin,
)


# Note that the class you subclass matters:
#
# * For command plugins (for adding new jirafs commands):
#     class Plugin(CommandPlugin):
#
# * For macro plugins (for transforming text content)
#     * If you're making a block tag:
#         class Plugin(BlockElementMacroPlugin)
#     * If you're making a void tag:
#         class Plugin(VoidElementMacroPlugin)
#
# * For other plugins (for processing uploaded files, etc)
#     class Plugin(GenericPlugin)
class Plugin(GenericPlugin):
    """ Converts Latex documents into PDFs when uploading to JIRA.

    """
    # See http://jirafs.readthedocs.org/en/latest/writing_plugins.html for
    # detailed information about how to write your own plugin.

    # Set this to the minimum version you've tested your plugin with
    MIN_VERSION = '1.10.0'
    # Set this to the first major version that this might break in (note
    # that Jirafs follows semantic versioning).
    MAX_VERSION = '2.0.0'

    # If you're creating a macro, set `COMPONENT_NAME` to the name match
    # the name you'd like to use.
    #
    #  COMPONENT_NAME = 'my-new-tag'

    def alter_file_upload(self, info):
        # Receives a single parameter `info` which is a 2-tuple of the
        # filename, and the file object.
        #
        # If you wanted to replace that file with another when uploading
        # to JIRA, you would return a *different* 2-tuple of a new filename
        # and a new file object to upload.  This is used by `jirafs-latex`,
        # `jirafs-graphviz` and `jirafs-pandoc` to automatically transform
        # uploaded documents into other formats.  See those repositories
        # for more information.
        #
        # Note that you will want to the filename mappings so we keep track
        # of the relationship between the file you're uploading and the file
        # stored on-disk by doing something like:
        #
        #   metadata = self.get_metadata()
        #   filename_map = metadata.get('filename_map', {})
        #   filename_map[new_filename] = filename
        #   metadata['filename_map'] = filename_map
        #   self.set_metadata(metadata)
        return info

    def execute_macro(self, data, **parameters):
        # This method is useful only if you're creating a macro plugin,
        # and when executed receives both the text content of the tag
        # (`data`) and any other arbitrary parameters as keyword arguments.
        #
        # Note that `data` will be `None` in `VoidElementMacroPlugin`
        # instances.
        #
        # This method should return text to replace your macro with
        # when writing the data to JIRA.
        return ''

    def validate(self):
        # Raise a `PluginValidationError` here if your plugin
        # needs to check the environment for various things before
        # being enabled.
        pass
