# Aplicação de contagem e armazenamento de dados do estoque de camisas - Versão GUI
import json
import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# área global de estilização de botões
 
# garante que o arquivo JSON ficará na mesma pasta do .py (fallback para cwd se necessário)
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
ARQUIVO_ESTOQUE = os.path.join(BASE_DIR, 'estoque_camisas.json')

# campo para armazenar os dados do estoque em variáveis
camisa_padrao_azul = "CAMISA AZUL PADRÃO"
tamanhos_camisa_azul_padrao = {'PP': 0, 'P': 0, 'M': 0, 'G': 0, 'GG': 0, 'XG': 0, 'XGG': 0}


camisa_amarela = "CAMISA AMARELA"
camisa_amarela_feminina = "CAMISA AMARELA FEMININA"
camisa_amarela_masculina = "CAMISA AMARELA MASCULINA"
tamanhos_camisa_amarela_feminina = {'PP': 0, 'P': 0, 'M': 0, 'G': 0, 'GG': 0, 'XG': 0, 'XGG': 0}
tamanhos_camisa_amarela_masculina = {'P': 0, 'M': 0, 'G': 0, 'GG': 0, 'XG': 0, 'XGG': 0}

camisa_tecnico = "CAMISA DE TÉCNICO"
tamanhos_camisa_tecnico = {'PP': 0, 'P': 0, 'M': 0, 'G': 0, 'GG': 0, 'XG': 0, 'XGG': 0}
calca_tecnico = "CALÇA DE TÉCNICO"
tamanhos_calca_tecnico = {'PP': 0, 'P': 0, 'M': 0, 'G': 0, 'GG': 0, 'XG': 0, 'XGG': 0}
bones = "BONES"
tamanhos_bones = {'Único': 0}

# Novas camisas solicitadas
camisa_yellow_heart = "YELLOW HEART"
tamanhos_camisa_yellow_heart = {'PP': 0, 'P': 0, 'M': 0, 'G': 0, 'GG': 0, 'XG': 0, 'XGG': 0}

camisa_polo = "POLO"
tamanhos_camisa_polo = {'PP': 0, 'P': 0, 'M': 0, 'G': 0, 'GG': 0, 'XG': 0, 'XGG': 0}

camisa_vc_feliz = "VC FELIZ"
tamanhos_camisa_vc_feliz = {'PP': 0, 'P': 0, 'M': 0, 'G': 0, 'GG': 0, 'XG': 0, 'XGG': 0}

camisa_babyclix = "BABYCLIX"
tamanhos_camisa_babyclix = {'PP': 0, 'P': 0, 'M': 0, 'G': 0, 'GG': 0, 'XG': 0, 'XGG': 0}

blusas_de_frio = "BLUSAS DE FRIO"
tamanhos_blusas_de_frio = {'PP': 0, 'P': 0, 'M': 0, 'G': 0, 'GG': 0, 'XG': 0, 'XGG': 0}

def salvar_dados_estoque():
    # usa nomes das constantes se disponíveis, senão usa strings padrões para evitar NameError
    amarela_key = globals().get('camisa_amarela', "CAMISA AMARELA")
    fem_key = globals().get('camisa_amarela_feminina', "CAMISA AMARELA FEMININA")
    masc_key = globals().get('camisa_amarela_masculina', "CAMISA AMARELA MASCULINA")

    estoque = {
        camisa_padrao_azul: tamanhos_camisa_azul_padrao,
        amarela_key: {
            fem_key: tamanhos_camisa_amarela_feminina,
            masc_key: tamanhos_camisa_amarela_masculina
        },
        camisa_tecnico: tamanhos_camisa_tecnico,
        calca_tecnico: tamanhos_calca_tecnico,
        bones: tamanhos_bones,
        camisa_yellow_heart: tamanhos_camisa_yellow_heart,
        camisa_polo: tamanhos_camisa_polo,
        camisa_vc_feliz: tamanhos_camisa_vc_feliz,
        camisa_babyclix: tamanhos_camisa_babyclix,
        blusas_de_frio: tamanhos_blusas_de_frio
    }
    try:
        with open(ARQUIVO_ESTOQUE, 'w', encoding='utf-8') as arquivo_json:
            json.dump(estoque, arquivo_json, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar arquivo de estoque: {e}")
        return False

def carregar_dados_estoque():
    global tamanhos_camisa_azul_padrao
    global tamanhos_camisa_amarela_feminina
    global tamanhos_camisa_amarela_masculina
    global tamanhos_camisa_tecnico
    global tamanhos_calca_tecnico
    global tamanhos_bones
    global tamanhos_camisa_yellow_heart
    global tamanhos_camisa_polo
    global tamanhos_camisa_vc_feliz
    global tamanhos_camisa_babyclix
    global tamanhos_blusas_de_frio
    try:
        if not os.path.exists(ARQUIVO_ESTOQUE):
            salvar_dados_estoque()
            return True

        with open(ARQUIVO_ESTOQUE, 'r', encoding='utf-8') as arquivo_json:
            estoque = json.load(arquivo_json)

        if isinstance(estoque, dict):
            if camisa_padrao_azul in estoque and isinstance(estoque[camisa_padrao_azul], dict):
                tamanhos_camisa_azul_padrao = estoque[camisa_padrao_azul]
            if camisa_amarela in estoque and isinstance(estoque[camisa_amarela], dict):
                amarelas = estoque[camisa_amarela]
                if camisa_amarela_feminina in amarelas and isinstance(amarelas[camisa_amarela_feminina], dict):
                    tamanhos_camisa_amarela_feminina = amarelas[camisa_amarela_feminina]
                if camisa_amarela_masculina in amarelas and isinstance(amarelas[camisa_amarela_masculina], dict):
                    tamanhos_camisa_amarela_masculina = amarelas[camisa_amarela_masculina]
            if camisa_tecnico in estoque and isinstance(estoque[camisa_tecnico], dict):
                tamanhos_camisa_tecnico = estoque[camisa_tecnico]
            if calca_tecnico in estoque and isinstance(estoque[calca_tecnico], dict):
                tamanhos_calca_tecnico = estoque[calca_tecnico]
            if bones in estoque and isinstance(estoque[bones], dict):
                tamanhos_bones = estoque[bones]
            if camisa_yellow_heart in estoque and isinstance(estoque[camisa_yellow_heart], dict):
                tamanhos_camisa_yellow_heart = estoque[camisa_yellow_heart]
            if camisa_polo in estoque and isinstance(estoque[camisa_polo], dict):
                tamanhos_camisa_polo = estoque[camisa_polo]
            if camisa_vc_feliz in estoque and isinstance(estoque[camisa_vc_feliz], dict):
                tamanhos_camisa_vc_feliz = estoque[camisa_vc_feliz]
            if camisa_babyclix in estoque and isinstance(estoque[camisa_babyclix], dict):
                tamanhos_camisa_babyclix = estoque[camisa_babyclix]
            if blusas_de_frio in estoque and isinstance(estoque[blusas_de_frio], dict):
                tamanhos_blusas_de_frio = estoque[blusas_de_frio]
        else:
            messagebox.showwarning("Aviso", "Formato inválido do arquivo de estoque. Usando estoque padrão e sobrescrevendo o arquivo.")
            salvar_dados_estoque()
        return True

    except json.JSONDecodeError:
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_path = ARQUIVO_ESTOQUE + f'.corrompido.{timestamp}'
        try:
            os.rename(ARQUIVO_ESTOQUE, backup_path)
        except Exception:
            pass
        messagebox.showwarning("Aviso", f"Arquivo de estoque corrompido. Movido para: {backup_path}\nCriando novo arquivo com estoque padrão.")
        salvar_dados_estoque()
        return True
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar estoque: {e}")
        return False

def centralizar_janela(janela):
    """Centraliza qualquer janela na tela."""
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'+{x}+{y}')

class EstoqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Estoque")
        self.root.geometry("700x500")
        
        # Carregar dados
        carregar_dados_estoque()
        
        # Criar interface
        self.criar_interface()
        
        # Centralizar janela principal
        centralizar_janela(self.root)
        
        # Bind para salvar ao fechar
        self.root.protocol("WM_DELETE_WINDOW", self.sair_aplicacao)
    
    def criar_interface(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="17")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar pesos do grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Título
        titulo = ttk.Label(
            main_frame, 
            text="SISTEMA DE ESTOQUE", 
            font=("Segoe UI", 32, "bold"))
        titulo.grid(
            row=0, 
            column=0, 
            columnspan=3, 
            pady=(20, 40))


        # Frame de seleção
        selecao_frame = ttk.LabelFrame(
            main_frame, 
            text="Selecionar Operação", 
            padding="90",
            )
        
        selecao_frame = ttk.LabelFrame(
            main_frame, 
            text="Selecionar Operação", 
            padding="35"
        )
        selecao_frame.grid(
            row=1, 
            column=1, 
            columnspan=3, 
            sticky=(tk.W, tk.E), 
            padx=(40, 40)
        )

        # Frame interno para centralizar os botões
        botoes_frame = ttk.Frame(selecao_frame)
        botoes_frame.pack(expand=True, fill='both')
        
        # Botões de operação
        style = ttk.Style()
        tk.Button(
         botoes_frame, 
            text="Adicionar Itens",
            relief="flat",
            bg="light grey",
            fg="black",
            width=17,
            activebackground="dark grey",
            activeforeground="white",
            command=self.abrir_adicionar,
            ).pack(expand=True, side=tk.LEFT, padx=2, pady=2)

        tk.Button(
            botoes_frame,
            text="Remover Itens",
            command=self.abrir_remover,
            relief="flat",
            bg="light grey",
            fg="black",
            width=17,
            activebackground="dark grey",
            activeforeground="white",
            ).pack(expand=True, side=tk.LEFT, padx=2, pady=2)
        
        tk.Button(
            botoes_frame, 
            text="Mostrar Estoque",
            command=self.mostrar_estoque,
            relief="flat",
            bg="light grey",
            fg="black",
            width=17,
            activebackground="dark grey",
            activeforeground="white",
            ).pack(expand=True, side=tk.LEFT, padx=2, pady=2)

        tk.Button(
            botoes_frame, 
            text="Sair",
            command=self.sair_aplicacao,
            width=17,
            relief="flat",
            bg="light grey",
            fg="black",
            activebackground= "dark grey",
            activeforeground= "white",
            ).pack(expand=True, side=tk.LEFT, padx=2, pady=2)
        

        self.flexbox = tk.Frame(self.root, bg="#d9d9d9", height=80)
        self.flexbox.grid(row=2, column=0, sticky="nsew", pady=0)  # sem fill
        # Configura o grid da janela pra permitir expansão
        self.root.grid_rowconfigure(2, weight=15)
        self.root.grid_columnconfigure(2, weight=15)

        # Área de texto para mostrar estoque
        # self.texto_estoque = scrolledtext.ScrolledText(main_frame, width=80, height=20, state=tk.DISABLED)
        # self.texto_estoque.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    def abrir_adicionar(self):
        self.janela_operacao("Adicionar")
    
    def abrir_remover(self):
        self.janela_operacao("Remover")
    
    def janela_operacao(self, operacao):
        janela = tk.Toplevel(self.root)
        janela.title(f"{operacao} Itens")
        janela.geometry("400x300")
        janela.transient(self.root)
        janela.grab_set()
        
        # Centralizar janela de operação
        centralizar_janela(janela)
        
        # Frame principal
        frame = ttk.Frame(janela, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Tipo de vestimenta
        ttk.Label(
            frame, 
            text="Tipo de Vestimenta:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        tipos = [
            "Camisa Azul Padrão",
            "Camisa Amarela Feminina", 
            "Camisa Amarela Masculina",
            "Camisa de Técnico",
            "Calça de Técnico",
            "Bones",
            "YELLOW HEART",
            "POLO",
            "VC FELIZ",
            "BABYCLIX",
            "BLUSAS DE FRIO"
        ]
        
        self.tipo_var = tk.StringVar()
        tipo_combo = ttk.Combobox(frame, textvariable=self.tipo_var, values=tipos, state="readonly")
        tipo_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        tipo_combo.bind('<<ComboboxSelected>>', lambda e: self.atualizar_tamanhos(frame))
        
        # Tamanho
        ttk.Label(frame, text="Tamanho:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.tamanho_var = tk.StringVar()
        self.tamanho_combo = ttk.Combobox(
            frame,
            textvariable=self.tamanho_var, 
            state="readonly")
        self.tamanho_combo.grid(
            row=1, 
            column=1, 
            sticky=(tk.W, tk.E), 
            pady=5, 
            padx=(10, 0))
        
        # Quantidade
        ttk.Label(frame, text="Quantidade:").grid(row=2, column=0, sticky=tk.W, pady=5)
        
        self.quantidade_var = tk.StringVar()
        quantidade_entry = ttk.Entry(frame, textvariable=self.quantidade_var)
        quantidade_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Botões
        botoes_frame = ttk.Frame(frame)
        botoes_frame.grid(
            row=3, column=0, 
            columnspan=2, 
            pady=20)
        
        tk.Button(
            botoes_frame, 
            text=operacao,
            relief="flat",
            bg="light grey",
            fg="black",
            activebackground="dark grey",
            activeforeground="white",
            command=lambda: self.executar_operacao(operacao, janela)
            ).pack(side=tk.LEFT, padx=22, pady=60)

        tk.Button(
            botoes_frame,
            text="Cancelar",
            relief="flat",
            bg="light grey",
            fg="black",
            activebackground="dark grey",
            activeforeground="white",
            command=janela.destroy
            ).pack(side=tk.LEFT, padx=5)
        frame.columnconfigure(1, weight=1)
        
        tk.Label(
            frame,
        ).grid(row=1, column=0, sticky=tk.Toplevel, pady=5)

    def atualizar_tamanhos(self, frame):
        tipo_selecionado = self.tipo_var.get()
        
        if tipo_selecionado == "Camisa Azul Padrão":
            tamanhos = list(tamanhos_camisa_azul_padrao.keys())
        elif tipo_selecionado == "Camisa Amarela Feminina":
            tamanhos = list(tamanhos_camisa_amarela_feminina.keys())
        elif tipo_selecionado == "Camisa Amarela Masculina":
            tamanhos = list(tamanhos_camisa_amarela_masculina.keys())
        elif tipo_selecionado == "Camisa de Técnico":
            tamanhos = list(tamanhos_camisa_tecnico.keys())
        elif tipo_selecionado == "Calça de Técnico":
            tamanhos = list(tamanhos_calca_tecnico.keys())
        elif tipo_selecionado == "Bones":
            tamanhos = list(tamanhos_bones.keys())
        elif tipo_selecionado == "YELLOW HEART":
            tamanhos = list(tamanhos_camisa_yellow_heart.keys())
        elif tipo_selecionado == "POLO":
            tamanhos = list(tamanhos_camisa_polo.keys())
        elif tipo_selecionado == "VC FELIZ":
            tamanhos = list(tamanhos_camisa_vc_feliz.keys())
        elif tipo_selecionado == "BABYCLIX":
            tamanhos = list(tamanhos_camisa_babyclix.keys())
        elif tipo_selecionado == "BLUSAS DE FRIO":
            tamanhos = list(tamanhos_blusas_de_frio.keys())
        else:
            tamanhos = []
        
        self.tamanho_combo['values'] = tamanhos
        if tamanhos:
            self.tamanho_combo.set(tamanhos[0])
    
    def executar_operacao(self, operacao, janela):
        try:
            # Validar entrada
            tipo_selecionado = self.tipo_var.get()
            tamanho = self.tamanho_var.get()
            quantidade_str = self.quantidade_var.get()
            
            if not tipo_selecionado or not tamanho or not quantidade_str:
                messagebox.showwarning("Aviso", "Preencha todos os campos!")
                return
            
            try:
                quantidade = int(quantidade_str)
                if quantidade <= 0:
                    messagebox.showwarning("Aviso", "Quantidade deve ser maior que zero!")
                    return
            except ValueError:
                messagebox.showwarning("Aviso", "Quantidade deve ser um número inteiro!")
                return
            
            # Determinar qual dicionário usar
            if tipo_selecionado == "Camisa Azul Padrão":
                dicionario = tamanhos_camisa_azul_padrao
                nome_tipo = camisa_padrao_azul
            elif tipo_selecionado == "Camisa Amarela Feminina":
                dicionario = tamanhos_camisa_amarela_feminina
                nome_tipo = camisa_amarela_feminina
            elif tipo_selecionado == "Camisa Amarela Masculina":
                dicionario = tamanhos_camisa_amarela_masculina
                nome_tipo = camisa_amarela_masculina
            elif tipo_selecionado == "Camisa de Técnico":
                dicionario = tamanhos_camisa_tecnico
                nome_tipo = camisa_tecnico
            elif tipo_selecionado == "Calça de Técnico":
                dicionario = tamanhos_calca_tecnico
                nome_tipo = calca_tecnico
            elif tipo_selecionado == "Bones":
                dicionario = tamanhos_bones
                nome_tipo = bones
            elif tipo_selecionado == "YELLOW HEART":
                dicionario = tamanhos_camisa_yellow_heart
                nome_tipo = camisa_yellow_heart
            elif tipo_selecionado == "POLO":
                dicionario = tamanhos_camisa_polo
                nome_tipo = camisa_polo
            elif tipo_selecionado == "VC FELIZ":
                dicionario = tamanhos_camisa_vc_feliz
                nome_tipo = camisa_vc_feliz
            elif tipo_selecionado == "BABYCLIX":
                dicionario = tamanhos_camisa_babyclix
                nome_tipo = camisa_babyclix
            elif tipo_selecionado == "BLUSAS DE FRIO":
                dicionario = tamanhos_blusas_de_frio
                nome_tipo = blusas_de_frio
            else:
                messagebox.showerror("Erro", "Tipo de vestimenta inválido!")
                return
            
            # Executar operação
            if operacao == "Adicionar":
                dicionario[tamanho] += quantidade
                mensagem = f"Adicionados {quantidade} unidades de {nome_tipo} tamanho {tamanho}"
            else:  # Remover
                if dicionario[tamanho] >= quantidade:
                    dicionario[tamanho] -= quantidade
                    mensagem = f"Removidos {quantidade} unidades de {nome_tipo} tamanho {tamanho}"
                else:
                    messagebox.showwarning("Aviso", "Quantidade insuficiente em estoque!")
                    return
            
            # Salvar e atualizar interface
            if salvar_dados_estoque():
                messagebox.showinfo("Sucesso", mensagem)
                # self.mostrar_estoque()  # Removida esta linha
                janela.destroy()
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao executar operação: {e}")
    
    def mostrar_estoque(self):
        # Abre uma janela modal com abas e Treeviews para cada categoria do estoque
        janela = tk.Toplevel(self.root)
        janela.title("Estoque")
        janela.geometry("700x500")
        janela.transient(self.root)
        janela.grab_set()
        
        # Centralizar janela de estoque
        centralizar_janela(janela)

        notebook = ttk.Notebook(janela)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        def criar_tree(frame, dados):
            tree_frame = ttk.Frame(frame)
            tree_frame.pack(fill=tk.BOTH, expand=True)

            # Configure style for better alignment
            style = ttk.Style()
            style.configure("Custom.Treeview", 
                           rowheight=25,
                           font=("Segoe UI", 10))
            style.configure("Custom.Treeview.Heading", 
                           font=("Segoe UI", 11, "bold"),
                           padding=(10, 5))

            # Create columns
            cols = ("tamanho", "quantidade")
            tree = ttk.Treeview(tree_frame, 
                       columns=cols, 
                       show="headings", 
                       selectmode="browse", 
                       style="Custom.Treeview")

            # Configure headings with center alignment
            tree.heading("tamanho", text="Tamanho", anchor=tk.CENTER)
            tree.heading("quantidade", text="Quantidade", anchor=tk.CENTER)

            # Configure columns with fixed widths and center alignment
            tree.column("tamanho", 
               width=200, 
               minwidth=100, 
               anchor=tk.CENTER, 
               stretch=True)
            tree.column("quantidade", 
                width=200, 
                minwidth=100, 
                anchor=tk.CENTER, 
                stretch=True)

            # Add scrollbar
            vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=vsb.set)

            # Pack the tree and scrollbar
            tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=5)
            vsb.pack(side=tk.RIGHT, fill=tk.Y, pady=5)

            # Insert data with center alignment - sem ordenação
            for t in dados.keys(): 
                quantidade_str = str(dados[t]).center(10)
                tree.insert("", tk.END, values=(t, quantidade_str))

            return tree

        # Aba: Camisa Azul Padrão
        aba_azul = ttk.Frame(notebook)
        notebook.add(aba_azul, text="Camisa Azul Padrão")
        criar_tree(aba_azul, tamanhos_camisa_azul_padrao)

        # Aba: Camisas Amarelas (Feminina e Masculina)
        aba_amarelas = ttk.Frame(notebook)
        notebook.add(aba_amarelas, text="Camisas Amarelas")
        # feminina
        lbl_fem = ttk.Label(
            aba_amarelas, 
            text="Feminina", 
            font=("Segoe UI", 10, "bold"))
        lbl_fem.pack(
            anchor=tk.W, 
            padx=6, 
            pady=(6, 0))
        criar_tree(
            aba_amarelas, 
            tamanhos_camisa_amarela_feminina)
        # masculina
        lbl_masc = ttk.Label(
            aba_amarelas, 
            text="Masculina", 
            font=("Segoe UI", 10, "bold"))
        lbl_masc.pack(
            anchor=tk.W, 
            padx=6, 
            pady=(12, 40))
        criar_tree(
            aba_amarelas, 
            tamanhos_camisa_amarela_masculina)

        # Aba: Técnico (Camisa)
        aba_tecnico_camisa = ttk.Frame(notebook)
        notebook.add(
            aba_tecnico_camisa, 
            text="Técnico - Camisa")
        criar_tree(
            aba_tecnico_camisa, 
            tamanhos_camisa_tecnico)

        # Aba: Técnico (Calça)
        aba_tecnico_calca = ttk.Frame(notebook)
        notebook.add(
            aba_tecnico_calca, 
            text="Técnico - Calça")
        criar_tree(
            aba_tecnico_calca, 
            tamanhos_calca_tecnico)

        # Aba: Bones
        aba_bones = ttk.Frame(notebook)
        notebook.add(
            aba_bones, 
            text="Bones")
        criar_tree(
            aba_bones, 
            tamanhos_bones)

        # Novas abas solicitadas
        aba_yellow = ttk.Frame(notebook)
        notebook.add(aba_yellow, text="YELLOW HEART")
        criar_tree(aba_yellow, tamanhos_camisa_yellow_heart)

        aba_polo = ttk.Frame(notebook)
        notebook.add(aba_polo, text="POLO")
        criar_tree(aba_polo, tamanhos_camisa_polo)

        aba_vc = ttk.Frame(notebook)
        notebook.add(aba_vc, text="VC FELIZ")
        criar_tree(aba_vc, tamanhos_camisa_vc_feliz)

        aba_babyclix = ttk.Frame(notebook)
        notebook.add(aba_babyclix, text="BABYCLIX")
        criar_tree(aba_babyclix, tamanhos_camisa_babyclix)

        aba_blusas = ttk.Frame(notebook)
        notebook.add(aba_blusas, text="BLUSAS DE FRIO")
        criar_tree(aba_blusas, tamanhos_blusas_de_frio)

        # Botão fechar
        btn_frame = ttk.Frame(janela)
        btn_frame.pack(
            fill=tk.X, 
            pady=8)
        tk.Button(
            btn_frame, 
            text="Fechar", 
            command=janela.destroy
            ).pack(
            side=tk.RIGHT, 
            padx=10)
    
    def sair_aplicacao(self):
        if salvar_dados_estoque():
            self.root.destroy()

def main():
    root = tk.Tk()
    app = EstoqueApp(root)
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()