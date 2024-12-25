from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE INDEX "idx_users_email_133a6f" ON "users" ("email");
        CREATE INDEX "idx_chats_project_8aab6a" ON "chats" ("project_id_id");
        CREATE INDEX "idx_links_user_id_bb3672" ON "links" ("user_id_id", "project_id_id", "chat_id_id");
        CREATE INDEX "idx_responces_prompt__7d3684" ON "responces" ("prompt_id_id");
        CREATE INDEX "idx_prompts_chat_id_3f9a37" ON "prompts" ("chat_id_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "idx_responces_prompt__7d3684";
        DROP INDEX "idx_prompts_chat_id_3f9a37";
        DROP INDEX "idx_users_email_133a6f";
        DROP INDEX "idx_links_user_id_bb3672";
        DROP INDEX "idx_chats_project_8aab6a";"""
