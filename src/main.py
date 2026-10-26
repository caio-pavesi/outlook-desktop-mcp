from datetime import datetime
from typing import Any

import win32com.client as win32
from mcp.server import MCPServer

# Initialize MCPServer
mcp = MCPServer("outlook")

# Constants
MAIL_ITEM = 0  # olMailItem
INBOX_FOLDER_ID = 6  # Outlook MAPI default Inbox folder
DATE_FORMAT = "%m/%d/%Y %I:%M %p"  # Format expected by Outlook's Restrict method


def _get_outlook() -> Any:
    """Connect to the local Outlook desktop app."""
    return win32.Dispatch("outlook.application")


def _get_namespace() -> Any:
    """Return the Outlook app's MAPI namespace."""
    return _get_outlook().GetNamespace("MAPI")


def _get_inbox() -> Any:
    """Return the default Inbox folder."""
    return _get_namespace().GetDefaultFolder(INBOX_FOLDER_ID)


def get_emails_by_date_range(
    start_date: datetime, end_date: datetime, folder: Any = None
) -> Any:
    """Return inbox emails received within [start_date, end_date], newest first."""
    folder = folder or _get_inbox()
    items = folder.Items
    items.Sort("[ReceivedTime]", True)

    restriction = (
        f"[ReceivedTime] >= '{start_date.strftime(DATE_FORMAT)}' "
        f"AND [ReceivedTime] <= '{end_date.strftime(DATE_FORMAT)}'"
    )
    return items.Restrict(restriction)


def format_email(email: Any) -> str:
    """Format an Outlook mail item into a readable string."""
    return f"""
From: {email.SenderName}
Subject: {email.Subject}
Received: {email.ReceivedTime}
EntryID: {email.EntryID}
Body: {email.Body}
"""


@mcp.tool()
async def get_emails(start_date: str, end_date: str) -> str:
    """Get inbox emails received within a date range.

    Args:
        start_date: Start of the range, e.g. "2026-10-01" or "2026-10-01 08:00"
        end_date: End of the range, e.g. "2026-10-26" or "2026-10-26 23:59"
    """
    try:
        start = datetime.fromisoformat(start_date)
        end = datetime.fromisoformat(end_date)
    except ValueError:
        return "Unable to parse dates. Use the format YYYY-MM-DD or YYYY-MM-DD HH:MM."

    emails = list(get_emails_by_date_range(start, end))

    if not emails:
        return "No emails found in this date range."

    return "\n---\n".join(format_email(email) for email in emails)


@mcp.tool()
async def reply_to_email(entry_id: str, body: str) -> str:
    """Reply to an email identified by its EntryID.

    Args:
        entry_id: The EntryID of the email to reply to, from get_emails output
        body: The reply message text
    """
    try:
        email = _get_namespace().GetItemFromID(entry_id)
    except Exception:
        return f"Could not find an email with EntryID: {entry_id}"

    reply = email.Reply()
    reply.Body = f"{body}\n\n{reply.Body}"
    reply.Send()

    return f"Reply sent to {email.SenderName} for subject '{email.Subject}'."


@mcp.tool()
async def reply_all_to_email(entry_id: str, body: str) -> str:
    """Reply all to an email identified by its EntryID.

    Args:
        entry_id: The EntryID of the email to reply to, from get_emails output
        body: The reply message text
    """
    try:
        email = _get_namespace().GetItemFromID(entry_id)
    except Exception:
        return f"Could not find an email with EntryID: {entry_id}"

    reply = email.ReplyAll()
    reply.Body = f"{body}\n\n{reply.Body}"
    reply.Send()

    return f"Reply-all sent for subject '{email.Subject}'."


@mcp.tool()
async def forward_email(entry_id: str, to: str, body: str = "") -> str:
    """Forward an email identified by its EntryID to one or more recipients.

    Args:
        entry_id: The EntryID of the email to forward, from get_emails output
        to: Recipient email address(es), separated by semicolons
        body: Optional message to include above the forwarded content
    """
    try:
        email = _get_namespace().GetItemFromID(entry_id)
    except Exception:
        return f"Could not find an email with EntryID: {entry_id}"

    forward = email.Forward()
    forward.To = to
    if body:
        forward.Body = f"{body}\n\n{forward.Body}"
    forward.Send()

    return f"Forwarded '{email.Subject}' to {to}."


@mcp.tool()
async def send_email(to: str, subject: str, body: str, cc: str = "") -> str:
    """Create and send a new email.

    Args:
        to: Recipient email address(es), separated by semicolons
        subject: Email subject
        body: Email message text
        cc: Optional CC email address(es), separated by semicolons
    """
    mail = _get_outlook().CreateItem(MAIL_ITEM)
    mail.To = to
    mail.Subject = subject
    mail.Body = body
    if cc:
        mail.CC = cc
    mail.Send()

    return f"Email '{subject}' sent to {to}."


if __name__ == "__main__":
    mcp.run(transport="stdio")
