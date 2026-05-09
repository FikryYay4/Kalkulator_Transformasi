// ===== LOGIC GATE VISUALIZER =====
// Generate SVG diagrams for logic gates and circuits

class LogicGateVisualizer {
    constructor() {
        this.gateWidth = 120;
        this.gateHeight = 80;
        this.padding = 20;
        this.wireLength = 40;
    }

    // Generate SVG for single logic gate
    generateGateSVG(gateType, input1, input2, output) {
        const width = 300;
        const height = 150;
        const centerX = width / 2;
        const centerY = height / 2;

        let svg = `<svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg" style="background: var(--bg-card); border-radius: 8px;">`;
        
        // Define gradients and styles
        svg += `
            <defs>
                <linearGradient id="gateGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:var(--primary);stop-opacity:1" />
                    <stop offset="100%" style="stop-color:var(--secondary);stop-opacity:1" />
                </linearGradient>
                <filter id="glow">
                    <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
                    <feMerge>
                        <feMergeNode in="coloredBlur"/>
                        <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                </filter>
            </defs>
        `;

        if (gateType === 'NOT') {
            // NOT gate - single input
            svg += this.drawNOTGate(centerX, centerY, input1, output);
        } else {
            // Two-input gates
            svg += this.drawTwoInputGate(gateType, centerX, centerY, input1, input2, output);
        }

        svg += '</svg>';
        return svg;
    }

    drawNOTGate(x, y, input, output) {
        let svg = '';
        
        // Input wire
        svg += `<line x1="${x - 80}" y1="${y}" x2="${x - 40}" y2="${y}" stroke="var(--text-secondary)" stroke-width="2"/>`;
        
        // Input label
        svg += `<text x="${x - 90}" y="${y + 5}" fill="var(--text-primary)" font-size="14" font-weight="bold">${input}</text>`;
        
        // Triangle (NOT gate shape)
        svg += `<polygon points="${x - 40},${y - 20} ${x - 40},${y + 20} ${x + 10},${y}" fill="url(#gateGradient)" stroke="var(--primary)" stroke-width="2" filter="url(#glow)"/>`;
        
        // Bubble (inversion)
        svg += `<circle cx="${x + 18}" cy="${y}" r="8" fill="white" stroke="var(--primary)" stroke-width="2"/>`;
        
        // Gate label
        svg += `<text x="${x - 25}" y="${y + 5}" fill="white" font-size="12" font-weight="bold">NOT</text>`;
        
        // Output wire
        svg += `<line x1="${x + 26}" y1="${y}" x2="${x + 80}" y2="${y}" stroke="var(--text-secondary)" stroke-width="2"/>`;
        
        // Output label
        svg += `<text x="${x + 85}" y="${y + 5}" fill="var(--primary)" font-size="16" font-weight="bold">${output}</text>`;
        
        return svg;
    }

    drawTwoInputGate(gateType, x, y, input1, input2, output) {
        let svg = '';
        
        // Input wires
        svg += `<line x1="${x - 100}" y1="${y - 20}" x2="${x - 60}" y2="${y - 20}" stroke="var(--text-secondary)" stroke-width="2"/>`;
        svg += `<line x1="${x - 100}" y1="${y + 20}" x2="${x - 60}" y2="${y + 20}" stroke="var(--text-secondary)" stroke-width="2"/>`;
        
        // Input labels
        svg += `<text x="${x - 115}" y="${y - 15}" fill="var(--text-primary)" font-size="14" font-weight="bold">${input1}</text>`;
        svg += `<text x="${x - 115}" y="${y + 25}" fill="var(--text-primary)" font-size="14" font-weight="bold">${input2}</text>`;
        
        // Gate shape based on type
        if (gateType === 'AND' || gateType === 'NAND') {
            // AND gate shape
            svg += `<path d="M ${x - 60} ${y - 30} L ${x - 20} ${y - 30} Q ${x + 20} ${y - 30} ${x + 20} ${y} Q ${x + 20} ${y + 30} ${x - 20} ${y + 30} L ${x - 60} ${y + 30} Z" fill="url(#gateGradient)" stroke="var(--primary)" stroke-width="2" filter="url(#glow)"/>`;
        } else if (gateType === 'OR' || gateType === 'NOR') {
            // OR gate shape
            svg += `<path d="M ${x - 60} ${y - 30} Q ${x - 40} ${y} ${x - 60} ${y + 30} Q ${x - 20} ${y + 20} ${x + 20} ${y} Q ${x - 20} ${y - 20} ${x - 60} ${y - 30}" fill="url(#gateGradient)" stroke="var(--primary)" stroke-width="2" filter="url(#glow)"/>`;
        } else if (gateType === 'XOR') {
            // XOR gate shape (OR with extra line)
            svg += `<path d="M ${x - 70} ${y - 30} Q ${x - 50} ${y} ${x - 70} ${y + 30}" fill="none" stroke="var(--primary)" stroke-width="2"/>`;
            svg += `<path d="M ${x - 60} ${y - 30} Q ${x - 40} ${y} ${x - 60} ${y + 30} Q ${x - 20} ${y + 20} ${x + 20} ${y} Q ${x - 20} ${y - 20} ${x - 60} ${y - 30}" fill="url(#gateGradient)" stroke="var(--primary)" stroke-width="2" filter="url(#glow)"/>`;
        }
        
        // Gate label
        svg += `<text x="${x - 35}" y="${y + 5}" fill="white" font-size="12" font-weight="bold" text-anchor="middle">${gateType}</text>`;
        
        // NAND/NOR bubble
        if (gateType === 'NAND' || gateType === 'NOR') {
            svg += `<circle cx="${x + 28}" cy="${y}" r="8" fill="white" stroke="var(--primary)" stroke-width="2"/>`;
            svg += `<line x1="${x + 36}" y1="${y}" x2="${x + 80}" y2="${y}" stroke="var(--text-secondary)" stroke-width="2"/>`;
        } else {
            svg += `<line x1="${x + 20}" y1="${y}" x2="${x + 80}" y2="${y}" stroke="var(--text-secondary)" stroke-width="2"/>`;
        }
        
        // Output label
        svg += `<text x="${x + 85}" y="${y + 5}" fill="var(--primary)" font-size="16" font-weight="bold">${output}</text>`;
        
        return svg;
    }

    // Generate circuit diagram
    generateCircuitSVG(gates) {
        if (!gates || gates.length === 0) return '';

        const gateSpacing = 180;
        const width = Math.max(600, gates.length * gateSpacing + 100);
        const height = 200;
        const startX = 80;
        const centerY = height / 2;

        let svg = `<svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg" style="background: var(--bg-card); border-radius: 8px; border: 2px solid var(--border-color);">`;
        
        // Define gradients
        svg += `
            <defs>
                <linearGradient id="circuitGateGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:var(--primary);stop-opacity:1" />
                    <stop offset="100%" style="stop-color:var(--secondary);stop-opacity:1" />
                </linearGradient>
                <filter id="circuitGlow">
                    <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
                    <feMerge>
                        <feMergeNode in="coloredBlur"/>
                        <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                </filter>
                <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill="var(--primary)" />
                </marker>
            </defs>
        `;

        // Draw each gate
        gates.forEach((gate, index) => {
            const x = startX + index * gateSpacing;
            const gateId = `G${index + 1}`;
            
            // Determine input positions
            const input1IsGate = gate.input1.startsWith('G');
            const input2IsGate = gate.input2 && gate.input2.startsWith('G');
            
            if (gate.gate === 'NOT') {
                svg += this.drawCircuitNOTGate(x, centerY, gate.input1, gateId, index);
            } else {
                svg += this.drawCircuitTwoInputGate(gate.gate, x, centerY, gate.input1, gate.input2, gateId, index);
            }
            
            // Draw connection wires from previous gates
            if (input1IsGate && index > 0) {
                const prevGateNum = parseInt(gate.input1.substring(1)) - 1;
                const prevX = startX + prevGateNum * gateSpacing;
                svg += `<line x1="${prevX + 60}" y1="${centerY}" x2="${x - 60}" y2="${centerY - 20}" stroke="var(--primary)" stroke-width="2" marker-end="url(#arrowhead)" stroke-dasharray="5,5"/>`;
            }
            
            if (input2IsGate && index > 0) {
                const prevGateNum = parseInt(gate.input2.substring(1)) - 1;
                const prevX = startX + prevGateNum * gateSpacing;
                svg += `<line x1="${prevX + 60}" y1="${centerY}" x2="${x - 60}" y2="${centerY + 20}" stroke="var(--primary)" stroke-width="2" marker-end="url(#arrowhead)" stroke-dasharray="5,5"/>`;
            }
        });

        // Final output indicator
        const lastX = startX + (gates.length - 1) * gateSpacing;
        svg += `<text x="${lastX + 80}" y="${centerY + 5}" fill="var(--primary)" font-size="18" font-weight="bold">OUTPUT</text>`;
        svg += `<circle cx="${lastX + 140}" cy="${centerY}" r="15" fill="var(--primary)" stroke="var(--primary-dark)" stroke-width="2" filter="url(#circuitGlow)"/>`;
        svg += `<text x="${lastX + 140}" y="${centerY + 6}" fill="white" font-size="14" font-weight="bold" text-anchor="middle">G${gates.length}</text>`;

        svg += '</svg>';
        return svg;
    }

    drawCircuitNOTGate(x, y, input, gateId, index) {
        let svg = '';
        
        // Input wire (only if not from previous gate)
        if (!input.startsWith('G') || index === 0) {
            svg += `<line x1="${x - 80}" y1="${y}" x2="${x - 40}" y2="${y}" stroke="var(--text-secondary)" stroke-width="2"/>`;
            svg += `<text x="${x - 90}" y="${y + 5}" fill="var(--text-primary)" font-size="12" font-weight="bold">${input}</text>`;
        }
        
        // Triangle
        svg += `<polygon points="${x - 40},${y - 15} ${x - 40},${y + 15} ${x + 5},${y}" fill="url(#circuitGateGradient)" stroke="var(--primary)" stroke-width="2"/>`;
        
        // Bubble
        svg += `<circle cx="${x + 12}" cy="${y}" r="7" fill="white" stroke="var(--primary)" stroke-width="2"/>`;
        
        // Gate label
        svg += `<text x="${x - 25}" y="${y - 25}" fill="var(--primary)" font-size="11" font-weight="bold">${gateId}: NOT</text>`;
        
        // Output wire
        svg += `<line x1="${x + 19}" y1="${y}" x2="${x + 60}" y2="${y}" stroke="var(--primary)" stroke-width="2"/>`;
        
        return svg;
    }

    drawCircuitTwoInputGate(gateType, x, y, input1, input2, gateId, index) {
        let svg = '';
        
        // Input wires (only if not from previous gates)
        if (!input1.startsWith('G') || index === 0) {
            svg += `<line x1="${x - 80}" y1="${y - 20}" x2="${x - 50}" y2="${y - 20}" stroke="var(--text-secondary)" stroke-width="2"/>`;
            svg += `<text x="${x - 95}" y="${y - 15}" fill="var(--text-primary)" font-size="12" font-weight="bold">${input1}</text>`;
        }
        
        if (!input2.startsWith('G') || index === 0) {
            svg += `<line x1="${x - 80}" y1="${y + 20}" x2="${x - 50}" y2="${y + 20}" stroke="var(--text-secondary)" stroke-width="2"/>`;
            svg += `<text x="${x - 95}" y="${y + 25}" fill="var(--text-primary)" font-size="12" font-weight="bold">${input2}</text>`;
        }
        
        // Gate shape (simplified for circuit)
        if (gateType === 'AND' || gateType === 'NAND') {
            svg += `<path d="M ${x - 50} ${y - 25} L ${x - 15} ${y - 25} Q ${x + 15} ${y - 25} ${x + 15} ${y} Q ${x + 15} ${y + 25} ${x - 15} ${y + 25} L ${x - 50} ${y + 25} Z" fill="url(#circuitGateGradient)" stroke="var(--primary)" stroke-width="2"/>`;
        } else if (gateType === 'OR' || gateType === 'NOR') {
            svg += `<path d="M ${x - 50} ${y - 25} Q ${x - 35} ${y} ${x - 50} ${y + 25} Q ${x - 15} ${y + 15} ${x + 15} ${y} Q ${x - 15} ${y - 15} ${x - 50} ${y - 25}" fill="url(#circuitGateGradient)" stroke="var(--primary)" stroke-width="2"/>`;
        } else if (gateType === 'XOR') {
            svg += `<path d="M ${x - 58} ${y - 25} Q ${x - 43} ${y} ${x - 58} ${y + 25}" fill="none" stroke="var(--primary)" stroke-width="2"/>`;
            svg += `<path d="M ${x - 50} ${y - 25} Q ${x - 35} ${y} ${x - 50} ${y + 25} Q ${x - 15} ${y + 15} ${x + 15} ${y} Q ${x - 15} ${y - 15} ${x - 50} ${y - 25}" fill="url(#circuitGateGradient)" stroke="var(--primary)" stroke-width="2"/>`;
        }
        
        // Gate label
        svg += `<text x="${x - 25}" y="${y + 4}" fill="white" font-size="10" font-weight="bold" text-anchor="middle">${gateType}</text>`;
        svg += `<text x="${x - 25}" y="${y - 35}" fill="var(--primary)" font-size="11" font-weight="bold" text-anchor="middle">${gateId}</text>`;
        
        // NAND/NOR bubble
        if (gateType === 'NAND' || gateType === 'NOR') {
            svg += `<circle cx="${x + 22}" cy="${y}" r="7" fill="white" stroke="var(--primary)" stroke-width="2"/>`;
            svg += `<line x1="${x + 29}" y1="${y}" x2="${x + 60}" y2="${y}" stroke="var(--primary)" stroke-width="2"/>`;
        } else {
            svg += `<line x1="${x + 15}" y1="${y}" x2="${x + 60}" y2="${y}" stroke="var(--primary)" stroke-width="2"/>`;
        }
        
        return svg;
    }
}

// Global instance
window.logicGateVisualizer = new LogicGateVisualizer();
