import sys
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from gemini_chatbot.bot import GeminiChatBot, MODEL_NAME

console = Console()

def print_help():
    console.print(
        Panel(
            "[bold cyan]/clear[/bold cyan] : 화면 정리\n"
            "[bold cyan]/help[/bold cyan]  : 도움말 보기\n"
            "[bold cyan]exit / quit / q[/bold cyan] : 챗봇 종료",
            title="명령어 안내",
            border_style="cyan"
        )
    )

def main():
    console.print(
        Panel(
            f"[bold green]Gemini Terminal Chatbot[/bold green] [dim](단일 질의응답 모드)[/dim]\n"
            f"모델: [bold yellow]{MODEL_NAME}[/bold yellow]\n"
            f"종료: 'exit' 또는 'quit' (도움말: '/help')",
            border_style="green"
        )
    )

    try:
        bot = GeminiChatBot()
    except ValueError as e:
        console.print(f"\n[bold red][설정 필요][/bold red]\n{e}\n")
        sys.exit(1)

    while True:
        try:
            user_input = console.input("\n[bold cyan]You > [/bold cyan]").strip()
            if not user_input:
                continue

            if user_input.lower() in ("exit", "quit", "q"):
                console.print("[bold yellow]챗봇을 종료합니다. 좋은 하루 되세요![/bold yellow]")
                break
            elif user_input == "/clear":
                console.clear()
                continue
            elif user_input == "/help":
                print_help()
                continue

            with console.status("[bold green]Gemini 답변 생성 중...[/bold green]"):
                response_text = bot.send_message(user_input)

            console.print("[bold magenta]Gemini > [/bold magenta]")
            console.print(Markdown(response_text))

        except KeyboardInterrupt:
            console.print("\n[bold yellow]챗봇을 종료합니다.[/bold yellow]")
            break
        except Exception as e:
            console.print(f"[bold red]오류 발생:[/bold red] {e}")

if __name__ == "__main__":
    main()
